from common.common import draw_graph
from common.imports import *
from common.globals import *

import community as community_louvain

# Function for generating randowm network
# Input: number of graphs, number of nodes, probability
# Returns: random graph
def generate_random_network(num=5, nodes=10, prob=0.5):
    # number of iterations
    num_subgraphs = num
    n = nodes  # number of nodes
    p = prob  # probability for edge
    connections_per_subgraph = 3  # number of connections per sub graph
    subgraph_connections_factor = 2  # factor to control the connections of sub graph

    subgraphs = []
    seeds = range(num_subgraphs)  # use different seeds to have more random network

    # generate subraphs
    for i in seeds:
        G = nx.erdos_renyi_graph(n, p, seed=i)
        subgraphs.append(G)

    # merge subgraphs into one random network
    final_graph = nx.Graph()
    node_offset = 0
    graph_node_mappings = []  # save multiple nodes of subgraph for bridge connections

    for i, G in enumerate(subgraphs):
        mapping = {node: node + node_offset for node in G.nodes()}  # shift node indices
        chosen_nodes = random.sample(list(mapping.values()),
                                     min(connections_per_subgraph, len(mapping)))  # pick multiple nodes
        graph_node_mappings.append(chosen_nodes)  # store representative nodes
        G = nx.relabel_nodes(G, mapping)
        final_graph = nx.compose(final_graph, G)  # merge into final graph
        node_offset += len(G.nodes())  # update offset

    # add random connections in network
    for i in range(num_subgraphs):
        target_indices = random.sample(range(num_subgraphs),
                                       min(subgraph_connections_factor, num_subgraphs - 1))  # randomly choose subgraph

        for target in target_indices:
            if i != target:  # avoid self loops
                for _ in range(connections_per_subgraph):
                    node_a = random.choice(graph_node_mappings[i])
                    node_b = random.choice(graph_node_mappings[target])
                    final_graph.add_edge(node_a, node_b)
    return final_graph