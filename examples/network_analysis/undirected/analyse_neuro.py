
from common.analysis import CommunityAnalysis
from common.network import NetworkManager

nm = NetworkManager(file_path="../../../data/neuro/average_connectivity_condition_1.txt", skiprows=4)
G = nm.get_graph()

ca = CommunityAnalysis(graph=G)
df = ca.run(["Louvain", "Girvan Newman", "Label Propagation", "Fast Label Propagation", "Greedy Modularity"])