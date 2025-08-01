from common.imports import *
from common.globals import *

from common.generator import generate_random_network
from common.analysis import open_graph_directed
# read graph
G = open_graph_directed(None, "../data/eu/email-EuAll.txt")

# check if directed
if not nx.is_directed(G):
    G = nx.DiGraph(G)

# check if multigraph
print("Je G MultiDiGraph?", isinstance(G, nx.MultiDiGraph))

# convert to digraf if multiu
if isinstance(G, nx.MultiDiGraph):
    G = nx.DiGraph(G)

# basic stats
num_nodes = len(G.nodes())  # vertices
num_edges = len(G.edges())  # edges
density = nx.density(G)  # density

# WCC
wcc = list(max(nx.weakly_connected_components(G), key=len))  # convert to list

print("Največja WCC vsebuje vozlišč:", len(wcc))

# filter WCC
largest_wcc_subgraph = G.subgraph(wcc).copy()
num_nodes_wcc = largest_wcc_subgraph.number_of_nodes()
num_edges_wcc = largest_wcc_subgraph.number_of_edges()

print("Število povezav v največji WCC (pravilno filtrirano):", num_edges_wcc)

# SCC
largest_scc_nodes = max(nx.strongly_connected_components(G), key=len)
largest_scc_subgraph = G.subgraph(largest_scc_nodes).copy()
num_nodes_scc = largest_scc_subgraph.number_of_nodes()
num_edges_scc = largest_scc_subgraph.number_of_edges()

# average clustering coef.
avg_clustering = nx.average_clustering(G)

# diameter
try:
    graph_diameter = nx.diameter(G)
except nx.NetworkXError:
    graph_diameter = "N/A"

# connected components
num_components = nx.number_weakly_connected_components(G)

# print data
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

print("Gostota:", nx.density(G))
print("Povprecna stopnja vozlisca:", np.mean([d for n, d in G.degree()]))
print("Polmer :", nx.radius(G))