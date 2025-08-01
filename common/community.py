from common.imports import *
import community as community_louvain  # Louvain metoda
from common.analysis import draw_graph

# Function for filtering components
# Input: components of graph, limit
# Returns: filtered components
def filter_components(components, limit):
    filtered = []
    for component in components:
        if len(component) > limit:
            filtered.append(component)

    return filtered

# Function to set community colors
# Input: Graph G, communities
# Returns: node colors for community
def get_community_colors(H, communities):
    num_communities = len(communities)
    cmap = cm.get_cmap('hsv', num_communities)  # 'tab20' or 'hsv', ...

    node_colors = [cmap(i) for i in H.nodes()]  # set node colors

    return node_colors

# Function for contracting communities
# Input: Graph G
# Returns: graph H
# Source: networkx
def contract_communities(G, communities, weight_attr='Weight'):
    """
    Given a graph G and a list of communities (each a set of nodes),
    create a new graph H where each community is contracted into a single node.
    - The new graph H will have one node per community, labeled by index.
    - Each node in H will have an attribute 'size' = number of original nodes in that community.
    - If edges exist between nodes in different communities, they are combined in H;
      their weights are summed under weight_attr.
    """
    H = nx.Graph()

    # 1) Add one node in H for each community, store community size
    for i, comm in enumerate(communities):
        H.add_node(i, size=len(comm))

    # 2) Create a mapping from original node -> community index
    node2comm = {}
    for i, comm in enumerate(communities):
        for node in comm:
            node2comm[node] = i

    # 3) For each edge in G, link the corresponding communities in H
    for u, v, data in G.edges(data=True):
        cu = node2comm[u]
        cv = node2comm[v]
        if cu != cv:
            w = data.get(weight_attr, 1)
            if H.has_edge(cu, cv):
                H[cu][cv][weight_attr] += w
            else:
                H.add_edge(cu, cv, **{weight_attr: w})

    return H


# Function for visualising louvain community detection
# Input: Graph G
def visualise_louvain(G):
    # community detection
    partition = community_louvain.best_partition(G)

    # graph coloring
    unique_communities = list(set(partition.values()))
    cmap = plt.cm.get_cmap("tab10", len(unique_communities))
    community_colors = {comm: cmap(i) for i, comm in enumerate(unique_communities)}
    node_colors = [community_colors[partition[node]] for node in G.nodes]

    # draw graph
    draw_graph(G, "Louvain community detection", node_colors, with_labels=False, node_size=40)