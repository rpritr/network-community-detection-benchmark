# 🕸️ Community Detection in Graphs

A Python project for analyzing network structures and detecting communities using various algorithms such as **Louvain**, **Leiden**, **Infomap**, and others.  
The project supports both **directed and undirected graphs**, computes network statistics, detects communities, and exports comparative evaluation results.

---

## 📁 Project Structure

```
community-detection/
├── cd_benchmark/       # Core modules for analysis, detection, statistics, visualization
├── run/                # Executable scripts (entry points)
├── data/               # Input graph datasets
├── examples/           # Example usage scripts and visualizations
├── requirements.txt    # Python dependencies
├── pyproject.toml      # Package configuration
├── README.md           # Project documentation
```

---

## Getting Started

### Installation

#### Option 1: Install from PyPI (coming soon)

```bash
pip install cd-benchmark
```

#### Option 2: Install from source

```bash
git clone https://github.com/rpritr/network-community-detection-benchmark.git
cd community-detection
pip install -e .
```

#### Option 3: Development setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Quick Start

After installation, you can use the package in your Python code:

```python
from cd_benchmark.analysis import CommunityAnalysis
import networkx as nx

# Create or load your graph
G = nx.karate_club_graph()

# Run community detection
ca = CommunityAnalysis(graph=G)
results = ca.run(algorithms=["Louvain", "Leiden", "Infomap"])
print(results)
```

### Run Examples

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

```python
from cd_benchmark.analysis import CommunityAnalysis

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

```python
from cd_benchmark.benchmark import CommunityBenchmark

cb = CommunityBenchmark(graph=G)  # or file="data/graph.txt"
df = cb.run()
cb.summarize()
cb.plot_all()  # plot and export analysis graphs
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

---

## Dataset Source

Sample networks in this project are based on the SNAP collection:

> Leskovec, J., & Krevl, A. (2014). *SNAP Datasets: Stanford Large Network Dataset Collection*. Retrieved from http://snap.stanford.edu/data
> 
## Notes on AI Assistance Disclosure

> Parts of this project ( code refactoring and documentation) were developed with the assistance of [ChatGPT](https://openai.com/chatgpt), based on the GPT-4o model (OpenAI, August 2025).
