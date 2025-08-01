import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import pandas as pd
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster
from scipy.spatial.distance import pdist
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import seaborn as sns
from cdlib.algorithms import leiden, infomap, spectral, walktrap, girvan_newman,eigenvector, ga, markov_clustering, paris, spectral
from networkx.algorithms.community import greedy_modularity_communities
from networkx.algorithms import community
import time
import random