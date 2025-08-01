
from common.analysis import evaluate, network_analysis

# do analysis on EU communication network
results = network_analysis(None, "../../../data/eu/email-EuAll.txt", directed=True)

print(results)

