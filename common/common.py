from common.imports import *
from common.globals import *


# Function for drawing graph using network x
# Input: Graph G, title, node color, labels flag and node size
def draw_graph(G, title, node_color = "lightblue", with_labels = "True", node_size = 500):
    plt.figure(figsize=(10, 8))
    pos = nx.spring_layout(G, seed=42)

    nx.draw(G, pos, with_labels=with_labels, node_color=node_color, edge_color='gray', node_size=node_size, font_size=8)
    plt.title(title)
    plt.show()

# Function for drawing network using networkx
# Input: Graph H, node colors, title
def draw_network(H, node_colors, title):
    node_sizes = [5 * H.nodes[i]['size'] for i in H.nodes()]
    plt.figure(figsize=(15, 8))

    # larger k to move nodes farther apart; increase iterations if needed
    pos = nx.spring_layout(H, k=3.0, iterations=100)

    nx.draw_networkx(
        H,
        pos=pos,
        with_labels=False,
        node_size=node_sizes,
        node_color=node_colors,
        edge_color='gray'
    )
    plt.title(title)
    plt.axis('off')
    plt.show()

# Function for drawing dendrogram for graph G
# Input: Graph G, linkage matrix, title, label x, label y
def draw_dendrogram(G, linkage_matrix, title, label_x, label_y):
    plt.figure(figsize=(10, 5))
    dendrogram(linkage_matrix, labels=list(G.nodes), leaf_rotation=90)
    plt.title(title)
    plt.xlabel(label_x)
    plt.ylabel(label_y)
    plt.show()


# Function to generate n distinct colors using the HSV colormap
# Input: n colors
# Returns: cmap color map with distinct colors
def generate_distinct_colors(n):
    cmap = plt.cm.get_cmap('hsv', n)
    return [cmap(i) for i in range(n)]
