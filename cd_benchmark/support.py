from cd_benchmark.imports import *
from cd_benchmark.globals import *

# Function for detecting community characteristigs
# Input: Graph G, iter: communities
# Returns: Average density, Average degree, Average clustering coefficient
def community_characteristics(G, communities):
    total_density = 0
    total_degree = 0
    total_clustering = 0
    count = 0
    # loop through communities and extract structure
    for community in communities:
        subgraph = G.subgraph(community)
        size = len(subgraph)

        if size > 1:  # avoid  errors for single-node communities
            total_density += nx.density(subgraph)
            total_degree += sum(dict(subgraph.degree()).values()) / size
            total_clustering += nx.average_clustering(subgraph)
            count += 1

    # compute averages
    avg_density = total_density / count if count > 0 else 0
    avg_degree = total_degree / count if count > 0 else 0
    avg_clustering = total_clustering / count if count > 0 else 0

    return avg_density, avg_degree, avg_clustering

# Function reading directed graph
# Input: graph/file, seperator, skip header rows
# Returns: Graph object
def open_graph_directed(graph=None, file=None, sep="\t", skip=4):
    # open graph by file or provided as Graph object
    if file:
        # read file and structure
        df = pd.read_csv(file, sep="\s+", header=None, skiprows=skip, names=["Node1", "Node2"])

        # print head and info
        print(df.head())
        print(df.info())

        # check if graph is directed
        if "Weight" in df.columns:
            G = nx.from_pandas_edgelist(df, source="Node1", target="Node2", edge_attr="Weight", create_using=nx.DiGraph())
        else:
            G = nx.from_pandas_edgelist(df, source="Node1", target="Node2", create_using=nx.DiGraph())
    elif graph:
        G = graph
    else:
        raise ValueError("No graph or file provided!")

    # Preverimo osnovne informacije o grafu
    print(f"Read graph: {len(G.nodes())} vertices, {len(G.edges())} edges")
    return G

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

# Function reading undirected graph
# Input: graph/file, seperator
# Returns: Graph object
def open_graph(graph, file, sep = '\t'):
    # import data if file path is provied
    if file:
        df = open_txt(file, sep)
        # create graph
        G = nx.from_pandas_edgelist(df, source='Node1', target='Node2', edge_attr='Weight')

    # read graph if graph is provided
    if graph:
        G = graph
    return G
