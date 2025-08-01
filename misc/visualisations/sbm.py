from common.analysis import evaluate, network_analysis
from common.common import draw_graph
from common.generator import generate_random_network
import networkx as nx

n = [50, 20, 100]

# bolj kontrastne verjetnosti: več povezav znotraj skupnosti, skoraj nič med skupnostmi
p = [
    [0.35, 0.01, 0.005],
    [0.01, 0.45, 0.01],
    [0.005, 0.01, 0.50]
]
G = nx.stochastic_block_model(n, p, seed=0)
draw_graph(G, "SBM graf", node_color="red", with_labels=True, node_size=200)
