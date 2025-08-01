
from common.imports import *
from common.globals import *

from common.generator import GraphGenerator
from common.visualization import GraphVisualizer

gen = GraphGenerator(num_subgraphs=4, nodes_per_subgraph=15, edge_prob=0.3)
G = gen.generate()

viz = GraphVisualizer(G)
viz.draw_graph("Graph G", node_color="lightblue", with_labels=False, node_size=40)


# do analysis on network
results = network_analysis(G, None)
print(results.to_string())