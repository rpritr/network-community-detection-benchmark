import networkx as nx
from common.analysis import CommunityAnalysis

G = nx.karate_club_graph()

ca = CommunityAnalysis(graph=G)
df = ca.run()