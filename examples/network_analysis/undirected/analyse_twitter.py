from cd_benchmark.analysis import CommunityAnalysis
from cd_benchmark.network import NetworkManager

nm = NetworkManager(file_path="../../../data/FakeNews-2010_Retweets_Graph.txt", skiprows=4)
G = nm.get_graph()

ca = CommunityAnalysis(graph=G)
df = ca.run(["Label Propagation", "Fast Label Propagation", "Leiden"])