
from common.analysis import evaluate, network_analysis

# do analysis on citation network
results = network_analysis(None, "../data/citation/cit-Patents.txt")
print(results)

