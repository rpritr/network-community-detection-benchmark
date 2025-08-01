from common.imports import *
from common.globals import *

from common.analysis import open_graph_directed
from common.statistics import GraphStats

# read graph
G = open_graph_directed(None, "../data/neuro/average_connectivity_condition_1.txt")

stats = GraphStats(G)
stats.compute()         # izračuna statistike in jih shrani v .stats
stats.print_summary()   # izpiše lepo prevedene rezultate