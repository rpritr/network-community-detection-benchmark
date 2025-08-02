from common.network import NetworkManager
from common.statistics import GraphStats

# read graph
nm = NetworkManager(file_path="../data/neuro/average_connectivity_condition_1.txt", directed=True, skiprows=4)
G = nm.get_graph()

stats = GraphStats(G)
stats.compute()         # compute graph stats
stats.print_summary()   # print graph stats summary