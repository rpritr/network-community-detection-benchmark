from common.imports import *
from common.globals import *

# Class for generating randowm network
# Input: number of graphs, number of nodes, probability
# Returns: random graph

class GraphGenerator:
    def __init__(self, num_subgraphs=5, nodes_per_subgraph=10, edge_prob=0.5,
                 connections_per_subgraph=3, connection_factor=2):
        self.num_subgraphs = num_subgraphs
        self.nodes_per_subgraph = nodes_per_subgraph
        self.edge_prob = edge_prob
        self.connections_per_subgraph = connections_per_subgraph
        self.connection_factor = connection_factor

    def generate(self):
        subgraphs = []
        seeds = range(self.num_subgraphs)

        for seed in seeds:
            G = nx.erdos_renyi_graph(self.nodes_per_subgraph, self.edge_prob, seed=seed)
            subgraphs.append(G)

        final_graph = nx.Graph()
        node_offset = 0
        graph_node_mappings = []

        for G in subgraphs:
            mapping = {node: node + node_offset for node in G.nodes()}
            chosen_nodes = random.sample(list(mapping.values()), min(self.connections_per_subgraph, len(mapping)))
            graph_node_mappings.append(chosen_nodes)
            G = nx.relabel_nodes(G, mapping)
            final_graph = nx.compose(final_graph, G)
            node_offset += len(G.nodes())

        for i in range(self.num_subgraphs):
            targets = random.sample(
                [x for x in range(self.num_subgraphs) if x != i],
                min(self.connection_factor, self.num_subgraphs - 1)
            )
            for target in targets:
                for _ in range(self.connections_per_subgraph):
                    node_a = random.choice(graph_node_mappings[i])
                    node_b = random.choice(graph_node_mappings[target])
                    final_graph.add_edge(node_a, node_b)

        return final_graph