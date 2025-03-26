import pandas as pd
import numpy as np
import networkx as nx
from common.analysis import evaluate, network_analysis
import matplotlib.pyplot as plt
import seaborn as sns
from common.generator import generate_random_network
import pandas as pd
import matplotlib.pyplot as plt

# Podatki o modularnosti algoritmov na različnih omrežjih
modularity_data = {
    "Algoritem": [
        "Louvain", "Label Propagation", "Fast Label propagation", "Leiden",
        "Informap", "Walktrap", "Greedy modularity", "Girvan Newman"
    ],
    "Omrežje nevroznanosti": [0.58457, 0.56520, 0.55826, 0.58460, 0.58300, 0.58080, 0.58280, 0.57640],
    "Zachary": [0.44077, 0.30949, 0.37273, 0.44490, 0.43210, 0.32316, 0.41096, 0.35806],
    "Erdős–Rényi": [0.76294, 0.70496, 0.74724, 0.76383, 0.75960, 0.75609, 0.74609, 0.64646],
    "Omrežje X": [0.90862, 0.81517, 0.80918, 0.91144, 0.84092, 0.85014, 0.90700, None],
    "Omrežje EU organizacije": [0.79091, 0.69716, 0.69585, 0.00838, 0.00796, None, None, None],
    "Omrežje citiranosti": [0.81151, 0.57483, 0.61951, 0.83249, None, None, None, None]
}

# Ustvarimo DataFrame
df_modularity = pd.DataFrame(modularity_data)

# Pretvorimo podatke v primernejši format za risanje
df_melted_modularity = df_modularity.melt(id_vars=["Algoritem"], var_name="Omrežje", value_name="Modularnost")

# Izrišemo graf
plt.figure(figsize=(12, 6))
for algoritem in df_modularity["Algoritem"]:
    subset = df_melted_modularity[df_melted_modularity["Algoritem"] == algoritem]
    plt.plot(subset["Omrežje"], subset["Modularnost"], marker='o', linestyle='-', label=algoritem)

plt.xlabel("Omrežje")
plt.ylabel("Modularnost")
plt.title("Primerjava modularnosti algoritmov na različnih omrežjih")
plt.legend(loc="upper left", bbox_to_anchor=(1, 1))
plt.xticks(rotation=45)
plt.grid(True, linestyle="--", linewidth=0.5)
plt.savefig("compare_modularity.jpg", dpi=300, bbox_inches="tight")
