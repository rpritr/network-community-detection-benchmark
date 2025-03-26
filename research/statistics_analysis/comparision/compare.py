import pandas as pd
import numpy as np
import networkx as nx
from common.analysis import evaluate, network_analysis
import matplotlib.pyplot as plt
import seaborn as sns
from common.generator import generate_random_network


data_final = {
    "Algoritem": [
        "Louvain", "Label Propagation", "Fast Label propagation", "Leiden",
        "Informap", "Walktrap", "Greedy modularity", "Girvan Newman"
    ],
    "Omrežje nevroznanosti": [0.0006111, 0.0002840, 0.0000022, 0.0009590, 0.0011369, 0.0003394, 0.0010408, 0.0000017],
    "Zachary": [0.0009990, 0.0001801, 0.0000025, 0.0010746, 0.0017194, 0.0004096, 0.0018034, 0.0000017],
    "Erdős–Rényi": [0.0033162, 0.0012709, 0.0000033, 0.0033184, 0.0047150, 0.0011552, 0.0094137, 0.0000030],
    "Omrežje X": [0.4767473, 0.3739566, 0.0000074, 0.2472860, 1.9601560, 0.8519429, 5.5470949, None],
    "Omrežje EU organizacije": [8.3547758, 4.7337946, 0.0000162, 4.4387278, 104.2351924, None, None, None],
    "Omrežje citiranosti": [4743.80048, 2291.033145, 0.00231385231, 436.1735771, None, None, None, None]
}

# Ustvarimo DataFrame
df_final = pd.DataFrame(data_final)

# Pretvorimo podatke v primernejši format za risanje
df_melted_final = df_final.melt(id_vars=["Algoritem"], var_name="Omrežje", value_name="Čas izvajanja")

# Izrišemo graf
plt.figure(figsize=(12, 6))
for algoritem in df_final["Algoritem"]:
    subset = df_melted_final[df_melted_final["Algoritem"] == algoritem]
    plt.plot(subset["Omrežje"], subset["Čas izvajanja"], marker='o', linestyle='-', label=algoritem)

plt.yscale("log")  # Logaritemska lestvica zaradi velikih razlik v časih izvajanja
plt.xlabel("Omrežje")
plt.ylabel("Čas izvajanja (s)")
plt.title("Primerjava časa izvajanja algoritmov na izbranih omrežjih")
plt.legend(loc="upper left", bbox_to_anchor=(1, 1))
plt.xticks(rotation=45)
plt.grid(True, which="both", linestyle="--", linewidth=0.5)
#plt.show()
plt.savefig("compare.jpg", dpi=300, bbox_inches="tight")
