
from common.imports import *
from common.globals import *

from common.analysis import network_analysis

# do analysis on citation network
results = network_analysis(None, "../../../data/citation/cit-Patents.txt")
print(results)

