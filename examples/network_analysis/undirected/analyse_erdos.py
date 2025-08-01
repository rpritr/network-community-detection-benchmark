
from common.imports import *
from common.globals import *

from common.analysis import network_analysis
from common.common import draw_graph
from common.generator import GraphGenerator
from common.statistics import get_stats
gen = GraphGenerator(num_subgraphs=4, nodes_per_subgraph=15, edge_prob=0.3)
G = gen.generate()
draw_graph(G, "ER povezan graf z več povezavami", node_color="lightblue", with_labels=False, node_size=40)

# do analysis on random network
results = network_analysis(G, None)
print(results.to_string())

