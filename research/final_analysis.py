import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pymcdm.methods import TOPSIS
from IPython.display import display

# Tvoje podatke naložimo v DataFrame
df = pd.DataFrame({
    "Network": ["Zachary", "Random", "Twitter", "Citation", "EU"],
    "Nodes": [34, 150, 14103, 3774768, 265214],
    "Edges": [78, 418, 13467, 16518948, 365570],
    "Louvain": [0.00100, 0.00384, 0.40382, 4743.80048, 9.62885],
    "Label Propagation": [0.00031, 0.00148, 0.35838, 2291.03314, 4.70192],
    "Fast Label Propagation": [0.00007, 0.00007, 0.00016, 0.00231, 0.00095],
    "Leiden": [0.00569, 0.00807, 0.22418, 436.17358, 4.98428],
    "Infomap": [0.00226, 0.00819, 1.80458, np.nan, 109.10740],  # Manjkajoče vrednosti zamenjane z np.nan
    "Walktrap": [0.00095, 0.00165, 0.83856, np.nan, np.nan],
    "Greedy Modularity": [0.00195, 0.01188, 5.31351, np.nan, np.nan],
    "Girvan Newman": [0.00006, 0.00007, np.nan, np.nan, np.nan],
})

# Normalizacija časa izvajanja na vozlišče in povezavo
for algo in ["Louvain", "Label Propagation", "Fast Label Propagation", "Leiden", "Infomap", "Walktrap", "Greedy Modularity", "Girvan Newman"]:
    df[f"{algo} per Node"] = df[algo] / df["Nodes"]
    df[f"{algo} per Edge"] = df[algo] / df["Edges"]

# Funkcija za vizualizacijo rasti časa izvajanja glede na velikost omrežja
def plot_scaling(df, algorithms):
    plt.figure(figsize=(10, 6))
    for algo in algorithms:
        plt.plot(df["Nodes"], df[algo], marker="o", label=algo)

    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("Število vozlišč (log scale)")
    plt.ylabel("Čas izvajanja (log scale)")
    plt.title("Čas izvajanja algoritmov glede na velikost omrežja")
    plt.legend()
    plt.show()

plot_scaling(df, ["Louvain", "Label Propagation", "Fast Label Propagation", "Leiden", "Infomap", "Walktrap", "Greedy Modularity", "Girvan Newman"])

# Vizualizacija modularnosti glede na velikost omrežja
plt.figure(figsize=(10, 6))
for algo in ["Louvain", "Label Propagation", "Fast Label Propagation", "Leiden", "Infomap", "Walktrap", "Greedy Modularity", "Girvan Newman"]:
    sns.scatterplot(data=df, x="Nodes", y=algo, label=algo)

plt.xscale("log")
plt.xlabel("Število vozlišč (log scale)")
plt.ylabel("Modularnost")
plt.title("Modularnost algoritmov glede na velikost omrežja")
plt.legend()
plt.show()
