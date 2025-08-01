
from common.imports import *
from common.globals import *

from common.analysis import network_analysis

# do analysis on X network
results = network_analysis(None, "../../../data/FakeNews-2010_Retweets_Graph.txt")
print(results)

