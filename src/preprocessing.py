import numpy as np
import pandas as pd
from pathlib import Path

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

if __name__ == "__main__":
    get_nodes_positions()