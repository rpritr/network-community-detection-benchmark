from common.support import open_graph, community_characteristics
from common.imports import *
from common.globals import *

class CommunityAnalysis:
    def __init__(self, graph=None, file=None, sep='\t', directed=False):
        self.graph = open_graph(graph=graph, file=file, sep=sep)
        self.results = []


    def evaluate(self, method_name, func, is_cdlib=False, *args, **kwargs):
        start_time = time.time()
        result = func(self.graph,*args, **kwargs)
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
        density, degree, clustering = community_characteristics(self.graph, communities)

        # compute modularity
        try:
            modularity = nx.community.modularity(self.graph, communities) if num_communities > 1 else None
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

    # Function for network analysis of community algorithms
    # Input: Graph G or file path, seperator, directed flag
    # Returns: DataFrame of comparision results
    def run(self, algorithms=None):

        if algorithms is None:
            algorithms = ["Louvain", "Leiden", "Infomap", "Girvan Newman", "Fast Label Propagation", "Walktrap", "Greedy Modularity"]

        available_algorithms = {
            "Louvain": (nx.community.louvain_communities, False),
            "Infomap": (infomap, True),
            "Leiden": (leiden, True),
            "Girvan Newman": (nx.community.girvan_newman, False),
            "Label Propagation": (nx.community.label_propagation_communities, False),
            "Fast Label Propagation": (nx.community.fast_label_propagation_communities, False),
            "Walktrap": (walktrap, True),
            "Greedy Modularity": (greedy_modularity_communities, False),
            # Dodaj druge metode po potrebi
        }

        for name in algorithms:
            if name not in available_algorithms:
                print(f"[WARN] Algorithm '{name}' not recognized.")
                continue
            func, is_cdlib = available_algorithms[name]
            self.results.append(self.evaluate(name, func, is_cdlib))



        # convert into DataFrame and export to CSV
        pd.DataFrame(self.results).to_csv("community_detection_results.csv", index=False)

        return pd.DataFrame(self.results)

