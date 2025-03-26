from common.imports import *
import networkx as nx
import matplotlib.pyplot as plt
from common.analysis import draw_graph
from common.generator import generate_random_network
from common.analysis import open_graph_directed
# Ustvarimo graf
G = open_graph_directed(None, "../../data/eu/email-EuAll.txt")

# Zagotovimo, da je usmerjen
if not nx.is_directed(G):
    G = nx.DiGraph(G)

# Preverimo, ali je graf večkratni graf (MultiDiGraph)
print("Je G MultiDiGraph?", isinstance(G, nx.MultiDiGraph))

# Če je graf MultiDiGraph, ga pretvorimo v običajen DiGraph
if isinstance(G, nx.MultiDiGraph):
    G = nx.DiGraph(G)

# Osnovne metrike
num_nodes = len(G.nodes())  # Število vozlišč
num_edges = len(G.edges())  # Število povezav
density = nx.density(G)  # Gostota mreže

# Največja šibko povezana komponenta (WCC)
wcc = list(max(nx.weakly_connected_components(G), key=len))  # Pretvorimo v seznam

print("Največja WCC vsebuje vozlišč:", len(wcc))  # Mora biti 224832

# Uporabimo pravilno metodo za filtriranje povezav v WCC
largest_wcc_subgraph = G.subgraph(wcc).copy()
num_nodes_wcc = largest_wcc_subgraph.number_of_nodes()
num_edges_wcc = largest_wcc_subgraph.number_of_edges()

print("Število povezav v največji WCC (pravilno filtrirano):", num_edges_wcc)  # Mora biti 395270

# Največja močno povezana komponenta (SCC)
largest_scc_nodes = max(nx.strongly_connected_components(G), key=len)
largest_scc_subgraph = G.subgraph(largest_scc_nodes).copy()
num_nodes_scc = largest_scc_subgraph.number_of_nodes()
num_edges_scc = largest_scc_subgraph.number_of_edges()

# Povprečni koeficient gručenja
avg_clustering = nx.average_clustering(G)

# Premer grafa (diameter)
try:
    graph_diameter = nx.diameter(G)
except nx.NetworkXError:
    graph_diameter = "N/A"  # Če graf ni povezan, premer ni definiran

# Število povezanih komponent
num_components = nx.number_weakly_connected_components(G)

# Izpis rezultatov
print("Število vozlišč:", num_nodes)
print("Število povezav:", num_edges)
print("Število vozlišč v največji WCC:", num_nodes_wcc)
print("Število povezav v največji WCC:", num_edges_wcc)
print("Število vozlišč v največji SCC:", num_nodes_scc)
print("Število povezav v največji SCC:", num_edges_scc)
print("Povprečni koeficient gručenja:", avg_clustering)
print("Diameter:", graph_diameter)
print("Število povezanih komponent:", num_components)
avg_clustering_directed = nx.average_clustering(G)
avg_clustering_undirected = nx.average_clustering(G.to_undirected())

print("Povprečni koeficient gručenja (usmerjen graf):", avg_clustering_directed)
print("Povprečni koeficient gručenja (neusmerjen graf):", avg_clustering_undirected)
triangles = sum(nx.triangles(G.to_undirected()).values()) // 3
print("Število trikotnikov:", triangles)
