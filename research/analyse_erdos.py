
from common.analysis import evaluate, network_analysis
from common.common import draw_graph
from common.generator import generate_random_network
from common.statistics import get_stats
from common.community import visualise_louvain
G = generate_random_network(15)
#draw_graph(G, "ER povezan graf z več povezavami", node_color="lightblue", with_labels=False, node_size=40)

# do analysis on random network
results = network_analysis(G, None)
print(results.to_string())

