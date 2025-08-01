import networkx as nx
import matplotlib.pyplot as plt
from common.analysis import evaluate, network_analysis
from common.common import draw_graph
from common.generator import generate_random_network


n = 100        # število vozlišč
k = 4         # vsako vozlišče povežemo s k najbližjimi sosedi
p = 0.3       # verjetnost prevezave povezave

# Ustvari graf
G = nx.watts_strogatz_graph(n, k, p)
pos = nx.circular_layout(G)

draw_graph(G, "Omrežje malega sveta", node_color="red", with_labels=True, node_size=200)
