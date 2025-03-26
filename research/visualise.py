import networkx as nx

from common.common import open_txt, draw_network
from common.community import contract_communities, get_community_colors, filter_components
from common.imports import *
from cdlib.algorithms import leiden
# import graph
#df = open_txt("../data/FakeNews-2010_Retweets_Graph.txt")
df = open_txt("../data/citation/cit-Patents.txt", "	")
G = nx.from_pandas_edgelist(df, source='Node1', target='Node2', edge_attr='Weight', create_using=nx.DiGraph())

communities_total = list(community.louvain_communities(G))
print("Number of Total Communities:", len(communities_total))

# get components
components = list(nx.weakly_connected_components(G))
print("Number of Total Components:", len(components))
print([len(c) for c in sorted(components, key=len, reverse=True)])

# filter components to max sub node size
large_components = filter_components(components, 5)
print("Number of Filtered Components:", len(large_components))
print([len(c) for c in sorted(large_components, key=len, reverse=True)])

components_union = set().union(*large_components)
subgraph = G.subgraph(components_union)

# detect communities
communities = list(community.louvain_communities(subgraph))
print("Number of Component Communities:", len(communities))

# contract communities
H = contract_communities(subgraph, communities)
print("Nodes in cluster graph:", H.number_of_nodes(), "Edges:", H.number_of_edges())

# set colors
node_colors = get_community_colors(H, communities)

# draw network
draw_network(H, node_colors, "Detekcija skupnosti na omrežju Twitter 2010")