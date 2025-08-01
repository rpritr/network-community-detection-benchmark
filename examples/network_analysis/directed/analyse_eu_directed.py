
from common.imports import *
from common.globals import *

# do analysis on EU communication network
results = network_analysis(None, "../../../data/eu/email-EuAll.txt", directed=True)

print(results)

