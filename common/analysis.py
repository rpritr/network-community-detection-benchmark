from common.imports import *
from common.globals import *
from common.common import open_txt

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


# Function for evaluating community detection based on method
# Input: algorithm/method name, method/algorithm call, flag for cdlib library, arguments for method call
# Returns: object with evaluation results { method, number of communities, max community size, average community size, modularity, average density, average degree, average clustering coefficient, execution time
def evaluate(method_name, func, is_cdlib=False, *args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        # check for method specifics and extract communities
        if method_name == "Girvan Newman":
            iteration = 3  # default iteration, change if required, TODO: pass as argument
            for i, communities in enumerate(result):
                if i == iteration - 1:
                    communities = [set(community) for community in communities]  # extract into set
                    break
        elif is_cdlib:
            communities = result.communities
        else:
            communities = list(result)

        # compute structure and size
        num_communities = len(communities)
        sizes = [len(c) for c in communities]
        max_size = max(sizes) if sizes else 0
        avg_size = sum(sizes) / num_communities if num_communities > 0 else 0
        density, degree, clustering = community_characteristics(args[0], communities)

        # compute modularity
        try:
            modularity = nx.community.modularity(args[0], communities) if num_communities > 1 else None
        except Exception as e:
            modularity = None

        # compute execution time
        exec_time = end_time - start_time

        # print data in console
        print(f"{method_name}:")
        print("  Communities:", num_communities)
        print("  Max size:", max_size)
        print("  Avg size:", avg_size)
        print("  Modularity:", modularity)
        print("  Avg. density:", density)
        print("  Avg. degree:", degree)
        print("  Avg. clustering:", clustering)

        print("  Time:", exec_time, "seconds")
        print("---------------")

        return {
            "Method": method_name,
            "Num Communities": num_communities,
            "Max Size": max_size,
            "Avg Size": avg_size,
            "Modularity": modularity,
            "Avg. density:": density,
            "Avg. degree:": degree,
            "Avg. clustering:": clustering,
            "Execution Time (s)": exec_time,
        }

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

# Function for network analysis of community algorithms
# Input: Graph G or file path, seperator, directed flag
# Returns: DataFrame of comparision results
def network_analysis(graph, file, sep = '\t', directed = False):
    # import data if file path is set
    if file:
        df = open_txt(file, sep)
        # create graph
        if not directed:
            G = nx.from_pandas_edgelist(df, source='Node1', target='Node2', edge_attr='Weight')
        else:
            G = nx.from_pandas_edgelist(df, source='Node1', target='Node2',
                                        edge_attr='Weight', create_using=nx.DiGraph())
    # read graph if graph is set
    if graph:
        G = graph
    # Print network statistics uncomment needed stats
    #stats(G)
    #get_stats(G)
    #visualise_louvain(G)

    # results frame
    results = []

    results.append(evaluate("Louvain", nx.community.louvain_communities, False, G))
    #if not G.is_directed():
    #    results.append(evaluate("Label Propagation", nx.community.label_propagation_communities, False, G))
    #results.append(evaluate("Fast Label Propagation", nx.community.fast_label_propagation_communities, False, G))
    results.append(evaluate("Leiden", leiden, True, G))
    results.append(evaluate("Infomap", infomap, True, G))
    #results.append(evaluate("Walktrap", walktrap, True, G))
    #results.append(evaluate("Greedy Modularity", greedy_modularity_communities, False, G))
    #results.append(evaluate("Girvan Newman", nx.community.girvan_newman, False, G))

    # convert into DataFrame and export to CSV
    df_results = pd.DataFrame(results)
    df_results.to_csv("community_detection_results.csv", index=False)
    return df_results