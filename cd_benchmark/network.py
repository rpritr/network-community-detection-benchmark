from cd_benchmark.globals import *

class NetworkManager:
    def __init__(self, file_path=None, graph=None, directed=False, sep="\s+", skiprows=0, has_weights=False):
        self.directed = directed
        self.sep = sep
        self.skiprows = skiprows
        self.has_weights = has_weights
        self.file_path = file_path
        self.graph = graph or self._load_graph()

    def _load_graph(self):
        if not self.file_path:
            raise ValueError("Either provide a graph or a file path.")

        df = pd.read_csv(
            self.file_path,
            sep=self.sep,
            skiprows=self.skiprows,
            header=None,
            names=["Node1", "Node2", "Weight"] if self.has_weights else ["Node1", "Node2"]
        )
        G_class = nx.DiGraph if self.directed else nx.Graph

        if self.has_weights:
            G = nx.from_pandas_edgelist(df, source="Node1", target="Node2", edge_attr="Weight", create_using=G_class())
        else:
            G = nx.from_pandas_edgelist(df, source="Node1", target="Node2", create_using=G_class())

        print(f"Loaded graph: {len(G.nodes())} nodes, {len(G.edges())} edges")
        return G

    def get_graph(self):
        return self.graph
