"""Load the FlyWire v783 proofread connectome as a directed, weighted graph.

Usage:
    python src/load.py --min-syn 5
"""
import argparse
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
PROC = ROOT / "data" / "processed"

PRE, POST = "pre_pt_root_id", "post_pt_root_id"



def get_nodes_positions():
    cols = ["pre_pt_root_id", "pre_pt_position_x", "pre_pt_position_y", "pre_pt_position_z"]

    nodes = np.load(RAW / "proofread_root_ids_783.npy")
    syn = pd.read_feather(RAW / "flywire_synapses_783.feather", columns=cols)

    pos = (syn[syn["pre_pt_root_id"].isin(nodes)]
        .groupby("pre_pt_root_id")[cols[1:]].mean()
        .reset_index()
        .rename(columns={"pre_pt_root_id": "root_id"}))

    pos.to_parquet("neuron_positions_pre.parquet", index=False)

    print(pos)


def load_nodes() -> np.ndarray:
    """IDs of all proofread neurons (int64)."""

    return np.load(RAW / "proofread_root_ids_783.npy")

def load_positions() -> pd.DataFrame:
    """Positions of all neurons (int64)."""
    
    conn = pd.read_parquet(
        PROC / "neuron_positions_pre.parquet",
        columns=["root_id", "pre_pt_position_x", "pre_pt_position_y", "pre_pt_position_z"],
    )

    return conn

def load_edges(min_syn: int = 1) -> pd.DataFrame:
    """One edge per ordered neuron pair, synapse counts summed over neuropils."""

    conn = pd.read_feather(
        RAW / "proofread_connections_783.feather",
        columns=[PRE, POST, "syn_count"],
    )
    edges = conn.groupby([PRE, POST], as_index=False)["syn_count"].sum()
    return edges[edges["syn_count"] >= min_syn].reset_index(drop=True)


def summary(nodes: np.ndarray, edges: pd.DataFrame) -> None:
    """Basic sanity checks of the node and edge lists."""
    
    endpoints = np.union1d(edges[PRE].unique(), edges[POST].unique())
    print(f"nodes (proofread neurons):       {len(nodes):,}")
    print(f"edges (neuron pairs):            {len(edges):,}")
    print(f"total synapses:                  {edges['syn_count'].sum():,}")
    print(f"nodes without any edge:          {len(np.setdiff1d(nodes, endpoints)):,}")
    print(f"edge endpoints not in node list: {len(np.setdiff1d(endpoints, nodes)):,}")
    print(f"self-loops (pre == post):        {(edges[PRE] == edges[POST]).sum():,}")


def to_igraph(nodes: np.ndarray, edges: pd.DataFrame):
    """Build an igraph Graph; vertex i corresponds to nodes[i]."""
    import igraph as ig

    index = pd.Index(nodes)
    src = index.get_indexer(edges[PRE])
    dst = index.get_indexer(edges[POST])
    if (src < 0).any() or (dst < 0).any():
        raise ValueError("Some edge endpoints are missing from the node list.")

    g = ig.Graph(n=len(nodes), edges=np.column_stack([src, dst]).tolist(), directed=True)
    g.vs["root_id"] = nodes.tolist()
    g.es["weight"] = edges["syn_count"].tolist()
    return g



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--min-syn", type=int, default=1,
                        help="minimum number of synapses per edge")
    args = parser.parse_args()

    nodes = load_nodes()
    edges = load_edges(args.min_syn)
    summary(nodes, edges)

    g = to_igraph(nodes, edges)
    print(g.summary())