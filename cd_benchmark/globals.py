from cdlib.algorithms import leiden, infomap, spectral, walktrap, girvan_newman,eigenvector, ga, markov_clustering, paris, spectral
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import networkx as nx
from networkx.algorithms.community import greedy_modularity_communities
from networkx.algorithms import community
import numpy as np
import pandas as pd
import random
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster
from scipy.spatial.distance import pdist
import seaborn as sns
from sklearn.metrics.pairwise import cosine_similarity
import time
