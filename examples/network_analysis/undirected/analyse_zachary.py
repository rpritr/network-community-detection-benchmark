import networkx as nx
from cd_benchmark.analysis import CommunityAnalysis

G = nx.karate_club_graph()

ca = CommunityAnalysis(graph=G)
df = ca.run()