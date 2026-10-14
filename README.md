# complex-networks-connectomics

Complex network analysis of the *Drosophila* connectome (FlyWire v783).

This project is developed for the *Complex Networks* course. It treats the whole-brain connectome of an adult female *Drosophila melanogaster* as a directed, weighted graph. Nodes are neurons, edges are chemical synaptic connections, and edge weights are synapse counts. The structure of the graph is analysed with standard tools of network science.

## Contents

- [Course tasks](#course-tasks)
- [Research questions](#research-questions)
- [Data](#data)
- [Preprocessing decisions](#preprocessing-decisions)
- [Repository structure](#repository-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Possible extensions](#possible-extensions)
- [Citations](#citations)
- [License](#license)

## Course tasks

### Task 1

- [ ] Shortest path between user-selected neurons
- [ ] Eulerian graph check (on a subgraph if needed) and Eulerian path
- [ ] Maximum flow between user-selected neurons (synapse counts as capacities)

### Further tasks

> TODO: analytical tasks prepared by the course instructor.

## Research questions

> TODO: define the research questions and planned analyses.

## Data

Raw data are **not** included in this repository because of their size. Download them from the original sources and place them in `data/raw/`.

| Dataset | Organism | Scope | Nodes | Source |
|---|---|---|---|---|
| FlyWire v783 | *D. melanogaster*, adult female | whole brain | 139,255 proofread neurons | [Codex](https://codex.flywire.ai), [Zenodo 10676866](https://zenodo.org/records/10676866) |

### Files used

| File | Content |
|---|---|
| `proofread_connections_783.feather` | Edge list: one row per neuron pair **and neuropil**, with synapse count (`syn_count`) and mean neurotransmitter probabilities |
| `proofread_root_ids_783.npy` | Node list: IDs of all proofread neurons |


For reference, the Codex release of v783 with a threshold of ≥5 synapses per connection contains 2,700,513 connections.

## Preprocessing decisions

`[Todo]`


## Repository structure

```
.
├── data/             # raw and processed data (git-ignored, reproducible from scripts)
├── notebooks/          # exploratory analyses
├── src/                # loading, preprocessing and analysis code
├── results/            # figures and tables
├── environment.yml
└── README.md
```

## Installation

```bash
git clone https://github.com/Alecz0/complex-networks-connectomics.git
cd complex-networks-connectomics
conda env create -f environment.yml
conda activate connectome
```



## Usage

> TODO: describe how to run preprocessing and analyses.


## Citations

If you use this repository, please cite the original data sources.

### Dataset

- FlyWire Consortium (2024). FlyWire Whole-brain Connectome Connectivity Data. Zenodo. https://doi.org/10.5281/zenodo.10676866

### FlyWire papers

- Dorkenwald, S. et al. (2024). Neuronal wiring diagram of an adult brain. *Nature*, 634, 124–138. https://doi.org/10.1038/s41586-024-07558-y
- Dorkenwald, S. et al. (2022). FlyWire: online community for whole-brain connectomics. *Nature Methods*, 19, 119–128. https://doi.org/10.1038/s41592-021-01330-0
- Zheng, Z. et al. (2018). A complete electron microscopy volume of the brain of adult *Drosophila melanogaster*. *Cell*, 174(3), 730–743. https://doi.org/10.1016/j.cell.2018.06.019
- Buhmann, J. et al. (2021). Automatic detection of synaptic partners in a whole-brain *Drosophila* electron microscopy data set. *Nature Methods*, 18, 771–774. https://doi.org/10.1038/s41592-021-01183-7

### Related work

- Lin, A. et al. (2024). Network statistics of the whole-brain connectome of *Drosophila*. *Nature*. https://doi.org/10.1038/s41586-024-07968-y

### Possible extensions

- Cook, S. J. et al. (2019). Whole-animal connectomes of both *Caenorhabditis elegans* sexes. *Nature*, 571, 63–71. https://doi.org/10.1038/s41586-019-1352-7
- Sexual dimorphism in the complete connectome of the *Drosophila* male central nervous system. *Cell* (2026). https://doi.org/10.1016/j.cell.2026.08.015

## License

> TODO: choose a license for the code (e.g. MIT). Data remain subject to the licenses of their original sources.