
from common.imports import *
from common.globals import *

from common.analysis import network_analysis

# do analysis on EU communication network
results = network_analysis(None, "../../../data/eu/email-EuAll.txt")

print(results)

