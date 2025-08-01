from common.analysis import evaluate, network_analysis
from common.common import draw_graph
from common.generator import generate_random_network
import networkx as nx
G = nx.erdos_renyi_graph(50, 0.5)

draw_graph(G, "Erdos Renyi graf", node_color="red", with_labels=True, node_size=200)
