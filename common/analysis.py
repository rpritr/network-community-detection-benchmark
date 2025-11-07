from common.support import open_graph, community_characteristics
from common.imports import *
from common.globals import *

class CommunityAnalysis:
    def __init__(self, graph=None, file=None, sep='\t', directed=False):
        self.graph = open_graph(graph=graph, file=file, sep=sep)
        self.results = []
        self.partitions = []
        self._pos_cache = None

    @staticmethod
    def _to_list_of_sets(obj):
        """Normalizira izhod različnih knjižnic v list[set]."""
        if obj is None:
            return []
        # cdlib: result.communities
        if hasattr(obj, "communities"):
            return [set(c) for c in obj.communities]
        # networkx generator (girvan_newman) ali navaden iterabilen izhod
        if isinstance(obj, (list, tuple, set)):
            # lahko je že list[iterable]
            if len(obj) > 0 and not isinstance(next(iter(obj)), (set, list, tuple)):
                # npr. pri nx.label_propagation_communities vrne generator setov
                return [set(c) for c in obj]
            else:
                return [set(c) for c in obj]
        # generator (npr. girvan_newman)
        try:
            peek = next(iter(obj))
            # če je generator skupnosti zaporedoma, vrni prvi element nazaj
            # (tukaj je pomembno, da evaluate za GN pokrije izbiro nivoja)
            raise TypeError
        except Exception:
            pass
        raise TypeError("Unsupported community structure format")

    @staticmethod
    def _labels_from_communities(communities):
        """list[set] -> dict {node: label} z zaporednimi etiketami 0..K-1"""
        labels = {}
        for i, comm in enumerate(communities):
            for n in comm:
                labels[n] = i
        return labels

    def _store_partition(self, method_name, communities):
        """Shrani particijo + vrne index."""
        labels = self._labels_from_communities(communities)
        self.partitions.append({
            "method": method_name,
            "communities": communities,
            "labels": labels
        })
        return len(self.partitions) - 1

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

        pidx = self._store_partition(method_name, communities)

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
            "partition_index": pidx,
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

# =========================
    # Vizualizacija
    # =========================
    def visualize(self, idx=-1, graph=None, seed=42, with_edges=True,
                  node_size=25, edge_alpha=0.12, linewidths=0.0, title=None, method=None):
        """Nariše particijo z indeksom idx iz self.partitions."""
        if not self.partitions:
            raise RuntimeError("No partitions stored. Run algorithms first.")
        if idx < 0:
            idx = len(self.partitions) + idx
        if idx < 0 or idx >= len(self.partitions):
            raise IndexError(f"Partition index out of range: {idx}")

        G = graph or self.graph
        part = self.partitions[idx]["labels"]

        # layout (keširaj, da so risbe primerljive)
        if self._pos_cache is None:
            random.seed(seed)
            self._pos_cache = nx.spring_layout(G, seed=seed)
        pos = self._pos_cache

        # barve po labelih
        labels = sorted(set(part.values()))
        color_map = {lab: i for i, lab in enumerate(labels)}
        node_colors = [color_map[part[n]] for n in G.nodes()]

        plt.figure(figsize=(10, 8))
        if with_edges:
            nx.draw_networkx_edges(G, pos, alpha=edge_alpha, width=0.5)
        nx.draw_networkx_nodes(
            G, pos,
            node_color=node_colors,
            node_size=node_size,
            linewidths=linewidths
        )
        plt.axis("off")
        if title:
            plt.title(title)

            plt.savefig(method, dpi=300, bbox_inches="tight")
            plt.close()  # zapre figuro, da ne pušča v pomnilniku

            plt.show()

    def visualize_by_method(self, method, how="max", metric="Modularity", **kwargs):
        """
        Najde vrstico v self.results za dano metodo (največja ali najmanjša vrednost metric)
        in nariše pripadajočo particijo.
        """
        if not self.results:
            raise RuntimeError("No results yet. Run algorithms first.")

        df = pd.DataFrame(self.results)
        sub = df[df["Method"] == method]
        if sub.empty:
            raise ValueError(f"No rows for method '{method}'.")

        row = sub.loc[sub[metric].idxmax()] if how == "max" else sub.loc[sub[metric].idxmin()]
        pidx = int(row["partition_index"])
        title = f"{method} — {how} {metric} ({row[metric]:.4f})" if row.get(metric) is not None else f"{method}"

        self.visualize(idx=pidx, title=title, **kwargs, method=method)
