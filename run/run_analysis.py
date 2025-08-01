
from common.imports import *
from common.globals import *
G = generate_random_network(15)
draw_graph(G, "Graph G", node_color="lightblue", with_labels=False, node_size=40)

# do analysis on network
results = network_analysis(G, None)
print(results.to_string())