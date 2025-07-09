from common.imports import *
from common.common import draw_graph
import numpy as np
import networkx as nx  # Poskrbi, da je networkx uvožen
import pandas as pd  # Za lepši izpis matrik

# Demo graph
G = nx.Graph([(1, 2), (1, 3), (2, 3), (3, 5), (3, 4), (4, 5), (6,7), (7,8), (8,6)])

# Plot graph
pos = nx.spring_layout(G)
draw_graph(G, "ER povezan graf z več povezavami", node_color="red", with_labels=True, node_size=500)

# Edges
edge_labels = {(u, v): f"{u}-{v}" for u, v in G.edges()}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='blue')

# Adjecency Matrix
A = nx.to_numpy_array(G, dtype=int)  # Pretvorba v numpy matriko
nodes = list(G.nodes())  # Seznam vozlišč
df_adj = pd.DataFrame(A, index=nodes, columns=nodes)

# Incidence matrix
I = nx.incidence_matrix(G, oriented=False).toarray()  # Pretvorba v gosto matriko
edges = list(G.edges())  # Seznam povezav
df_inc = pd.DataFrame(I, index=nodes, columns=[f"{e[0]}-{e[1]}" for e in edges])

# Print
print("Adjecency matrix:")
print(df_adj.to_string())

print("\nIncidence matrix:")
print(df_inc.to_string())