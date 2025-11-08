from cd_benchmark.globals import *

class GraphStats:
    def __init__(self, graph):
        self.G = graph
        self.stats = {}

    def compute(self):
        G = self.G
        self.stats["num_nodes"] = len(G.nodes())
        self.stats["num_edges"] = len(G.edges())
        self.stats["density"] = nx.density(G)
        self.stats["triangles"] = sum(nx.triangles(G.to_undirected()).values()) // 3
        self.stats["avg_node_degree"] = np.mean([d for n, d in G.degree()])

        if nx.is_directed(G):
            wcc = max(nx.weakly_connected_components(G), key=len)
        else:
            wcc = max(nx.connected_components(G), key=len)

        largest_wcc = G.subgraph(wcc)
        self.stats["wcc_nodes"] = len(largest_wcc.nodes())
        self.stats["wcc_edges"] = len(largest_wcc.edges())

        if nx.is_directed(G):
            scc = max(nx.strongly_connected_components(G), key=len)
            largest_scc = G.subgraph(scc)
            self.stats["scc_nodes"] = len(largest_scc.nodes())
            self.stats["scc_edges"] = len(largest_scc.edges())
        else:
            self.stats["scc_nodes"] = "N/A"
            self.stats["scc_edges"] = "N/A"

        self.stats["avg_clustering"] = nx.average_clustering(G)

        try:
            self.stats["diameter"] = nx.diameter(G)
        except nx.NetworkXError:
            self.stats["diameter"] = "N/A"

        try:
            self.stats["radius"] = nx.radius(G)
        except nx.NetworkXError:
            self.stats["radius"] = "N/A"

        self.stats["num_components"] = (
            nx.number_weakly_connected_components(G)
            if nx.is_directed(G)
            else nx.number_connected_components(G)
        )

        return self.stats

    def print_summary(self):
        labels = {
            "num_nodes": "Nodes: ",
            "num_edges": "Edges: ",
            "density": "Density: ",
            "wcc_nodes": "Nodes in largest WCC: ",
            "wcc_edges": "Edges in largest WCC: ",
            "scc_nodes": "Nodes in largest SCC: ",
            "scc_edges": "Edges in largest SCC: ",
            "avg_clustering": "Average Clustering Coeficient: ",
            "diameter": "Diameter: ",
            "radius": "Radius: ",
            "triangles": "Triangles: ",
            "avg_node_degree": "Average Node Degree: ",
            "num_components" : "Connected Components: "
        }

        for key, value in self.stats.items():
            print(f"{labels.get(key, key)}: {value}")