from common.analysis import CommunityAnalysis
from common.network import NetworkManager

nm = NetworkManager(file_path="../../../data/eu/email-EuAll.txt", directed=True, skiprows=4)
G = nm.get_graph()

ca = CommunityAnalysis(graph=G)
df = ca.run()
