
from common.imports import *
from common.globals import *

from common.analysis import network_analysis

# do analysis on EU communication network
results = network_analysis(None, "../../../data/neuro/average_connectivity_condition_1.txt", " ")

print(results)

