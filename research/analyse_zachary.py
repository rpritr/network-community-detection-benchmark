import networkx as nx

from common.analysis import evaluate, network_analysis
from common.common import draw_graph
from common.generator import generate_random_network

G = nx.karate_club_graph()
# draw_graph(G, "ER povezan graf z več povezavami", node_color="lightblue", with_labels=False, node_size=40)

# do analysis on Zachary network
results = network_analysis(G, None)
print(results.to_string())


