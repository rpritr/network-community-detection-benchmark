from common.imports import *
import networkx as nx
import matplotlib.pyplot as plt

# Random graph
G = nx.erdos_renyi_graph(20, 0.5)

# Basic matrix
num_nodes = len(G.nodes())  # Vertices
num_edges = len(G.edges())  # Edges
density = nx.density(G)  # Density

# WCC
if nx.is_directed(G):
    wcc = max(nx.weakly_connected_components(G), key=len)
else:
    wcc = max(nx.connected_components(G), key=len)

largest_wcc_subgraph = G.subgraph(wcc)
num_nodes_wcc = len(largest_wcc_subgraph.nodes())  # Vertices in WCC
num_edges_wcc = len(largest_wcc_subgraph.edges())  # Edges in WCC

# SCC - directed
if nx.is_directed(G):
    scc = max(nx.strongly_connected_components(G), key=len)
    largest_scc_subgraph = G.subgraph(scc)
    num_nodes_scc = len(largest_scc_subgraph.nodes())  # Veritces in SCC
    num_edges_scc = len(largest_scc_subgraph.edges())  # Edges in SCC
else:
    num_nodes_scc = "N/A"
    num_edges_scc = "N/A"

# Avg. Clustering coeficient
avg_clustering = nx.average_clustering(G)

# Diameter
try:
    graph_diameter = nx.diameter(G)
except nx.NetworkXError:
    graph_diameter = "N/A"

# WCC
num_components = nx.number_connected_components(G) if not nx.is_directed(G) else nx.number_weakly_connected_components(G)

# Degrees
degrees = [d for n, d in G.degree()]
plt.hist(degrees, bins=range(min(degrees), max(degrees) + 1), alpha=0.75, edgecolor="black")
plt.xlabel("Stopnja vozlišč")
plt.ylabel("Število vozlišč")
plt.title("Porazdelitev stopenj vozlišč")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()

# Print
print("Število vozlišč:", num_nodes)
print("Število povezav:", num_edges)
print("Število vozlišč v največji WCC:", num_nodes_wcc)
print("Število povezav v največji WCC:", num_edges_wcc)
print("Število vozlišč v največji SCC:", num_nodes_scc)
print("Število povezav v največji SCC:", num_edges_scc)
print("Povprečni koeficient gručenja:", avg_clustering)
print("Diameter:", graph_diameter)
print("Število povezanih komponent:", num_components)