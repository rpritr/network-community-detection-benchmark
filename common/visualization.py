import matplotlib.pyplot as plt
import networkx as nx

class GraphVisualizer:
    def __init__(self, graph):
        self.graph = graph

    def draw_graph(self, title, node_color="lightblue", with_labels=True, node_size=500):
        plt.figure(figsize=(10, 8))
        pos = nx.spring_layout(self.graph, seed=42)
        nx.draw(self.graph, pos, with_labels=with_labels, node_color=node_color, edge_color='gray',
                node_size=node_size, font_size=8)
        plt.title(title)
        plt.show()