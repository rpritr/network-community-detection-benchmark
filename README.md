# 🕸️ Community Detection in Graphs

A Python project for analyzing network structures and detecting communities using various algorithms such as **Louvain**, **Leiden**, **Infomap**, and others.  
The project supports both **directed and undirected graphs**, computes network statistics, detects communities, and exports comparative evaluation results.

---

## 📁 Project Structure

```
community-detection/
├── common/             # Core modules for analysis, detection, statistics, visualization
├── run/                # Executable scripts (entry points)
├── data/               # Input graph datasets
├── examples/           # Example usage scripts and visualizations
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
```

---

## Getting Started

### 1. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Run community detection example

```bash
python -m run.run_statistics
```

Or run the full benchmarking with configurable algorithms:

```bash
python -m run.run_analysis
```

---

## 🔧 Features

- Load graphs from edge list text files (directed or undirected)
- Compute network statistics:
  - Node and edge count
  - Largest WCC/SCC components
  - Clustering coefficient
  - Graph density, diameter, and radius
- Community detection algorithms:
  - Louvain
  - Leiden
  - Infomap
  - Walktrap
  - Girvan-Newman
  - Greedy modularity
  - Label Propagation
  - Fast Label Propagation
- Graph visualization (with Matplotlib / NetworkX)
- Export results to CSV for analysis and comparison

---

## Community Analysis

You can instantiate and run custom analyses as follows:

```
from common.cd_analysis import CommunityAnalysis

ca = CommunityAnalysis(graph=G)  # or file="data/graph.txt"
df = ca.run(algorithms=["Louvain", "Infomap"])
```

Supported algorithms:
```
["Louvain", "Leiden", "Infomap", "Girvan Newman", "Greedy Modularity", "Walktrap", "Label Propagation", "Fast Label Propagation"]
```

---

## Community Benchmark

You can run a full benchmark on 100 iterations as follows:

```
from common.cd_analysis import CommunityBenchmark

ca = CommunityBenchmark(graph=G)  # or file="data/graph.txt"
df = ca.run()
ca.summarize()
ca.plot_all() # plot and export analysis graph
```


## Sample Datasets

Example graph format (`cit-Patents.txt`):

```
Node1 Node2
12    14
15    17
...
```

Each line represents a directed edge in the network.

---

## Dependencies

Install all required packages from `requirements.txt`:

> Note: Some community detection methods in `cdlib` may require additional system-level libraries such as `graph-tool` or `infomap`.

---

## Author

**Robi Pritržnik** (2025)  
🔗 [pritrznik.si](https://pritrznik.si)  
📧 Contact: robi@pritrznik.si

---

## License

This project is intended for **research and educational purposes only**.  
Feel free to fork and extend under appropriate attribution.