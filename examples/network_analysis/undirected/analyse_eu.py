from cd_benchmark.analysis import CommunityAnalysis
from cd_benchmark.network import NetworkManager

nm = NetworkManager(file_path="../../../data/eu/email-EuAll.txt", skiprows=4)
G = nm.get_graph()

ca = CommunityAnalysis(graph=G)
df = ca.run()