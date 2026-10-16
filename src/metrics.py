import numpy as np
import pandas as pd


def neighborhood_growth(g, v: int, max_depth: int = 6) -> pd.DataFrame:
    """Share of vertices and edges within k hops of v (direction ignored)."""
    
    dist = np.array(g.distances(source=v, mode="all")[0], dtype=float)
    edges = np.array(g.get_edgelist())
    edge_depth = np.maximum(dist[edges[:, 0]], dist[edges[:, 1]])

    rows = []
    for k in range(1, max_depth + 1):
        nv = int((dist <= k).sum())
        ne = int((edge_depth <= k).sum())
        rows.append({"depth": k, "vertices": nv, "vertices_frac": nv / g.vcount(),
                     "edges": ne, "edges_frac": ne / g.ecount()})
    return pd.DataFrame(rows)