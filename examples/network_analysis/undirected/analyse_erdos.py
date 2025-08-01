from common.imports import *
from common.visualization import GraphVisualizer
from common.generator import GraphGenerator

gen = GraphGenerator(num_subgraphs=4, nodes_per_subgraph=15, edge_prob=0.3)
G = gen.generate()

viz = GraphVisualizer(G)
viz.draw_graph( "ER povezan graf z več povezavami", node_color="lightblue", with_labels=False, node_size=40)

# do analysis on random network
results = network_analysis(G, None)
print(results.to_string())

