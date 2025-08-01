from common.imports import *
from common.globals import *

# Function for reading graph from txt
# Input: txt path
# Returns: df datatype for CSV
def open_txt(path, sep):
    # Preberemo datoteko brez določanja števila stolpcev
    df = pd.read_csv(
        path,
        sep=sep, # seperator in CSV file
        comment="#",  # ignore comments in file
        header=None  # no header in file
    )

    # check if weight exists
    if df.shape[1] == 2:
        df.columns = ['Node1', 'Node2']
        df['Weight'] = 1  # default length for weighted graph
    elif df.shape[1] == 3:
        df.columns = ['Node1', 'Node2', 'Weight']
    else:
        raise ValueError("File does not have required columns, 3 columns required.")

    # convert into right types
    df = df.astype({'Node1': int, 'Node2': int, 'Weight': int})

    return df

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

# Function to print number of edges and nudes of graph
# Input: Graph G
def stats(G):
    print("Nodes: ", nx.number_of_nodes(G))
    print("Edges: ", nx.number_of_edges(G))

# Function to generate n distinct colors using the HSV colormap
# Input: n colors
# Returns: cmap color map with distinct colors
def generate_distinct_colors(n):
    cmap = plt.cm.get_cmap('hsv', n)
    return [cmap(i) for i in range(n)]
