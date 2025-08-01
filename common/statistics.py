from common.imports import *
import networkx as nx

# Ustvarimo graf
def get_stats(G):
    # Osnovne metrike
    num_nodes = len(G.nodes())  # Število vozlišč
    num_edges = len(G.edges())  # Število povezav
    density = nx.density(G)  # Gostota mreže

    # Največja šibko povezana komponenta (WCC)
    if nx.is_directed(G):
        wcc = max(nx.weakly_connected_components(G), key=len)
    else:
        wcc = max(nx.connected_components(G), key=len)

    largest_wcc_subgraph = G.subgraph(wcc)
    num_nodes_wcc = len(largest_wcc_subgraph.nodes())  # Število vozlišč v največji WCC
    num_edges_wcc = len(largest_wcc_subgraph.edges())  # Število povezav v največji WCC

    # Največja močno povezana komponenta (SCC) - samo za usmerjene grafe
    if nx.is_directed(G):
        scc = max(nx.strongly_connected_components(G), key=len)
        largest_scc_subgraph = G.subgraph(scc)
        num_nodes_scc = len(largest_scc_subgraph.nodes())  # Število vozlišč v največji SCC
        num_edges_scc = len(largest_scc_subgraph.edges())  # Število povezav v največji SCC
    else:
        num_nodes_scc = "N/A"
        num_edges_scc = "N/A"

    # Povprečni koeficient gručenja
    avg_clustering = nx.average_clustering(G)

    # Premer grafa (diameter)
    try:
        graph_diameter = nx.diameter(G)
    except nx.NetworkXError:
        graph_diameter = "N/A"  # Če graf ni povezan, premer ni definiran

    # Število povezanih komponent
    num_components = nx.number_connected_components(G) if not nx.is_directed(G) else nx.number_weakly_connected_components(G)

    # Stopnje vozlišč
    #degrees = [d for n, d in G.degree()]
    #plt.hist(degrees, bins=range(min(degrees), max(degrees) + 1), alpha=0.75, edgecolor="black")
    #plt.xlabel("Stopnja vozlišč")
    #plt.ylabel("Število vozlišč")
    #plt.title("Porazdelitev stopenj vozlišč")
    #plt.grid(axis="y", linestyle="--", alpha=0.7)
    #plt.show()



    # Poiščemo povezane komponente
    components = list(nx.connected_components(G)) if not nx.is_directed(G) else list(nx.weakly_connected_components(G))

    # Določimo barve za posamezne komponente
    color_map = {}
    for i, component in enumerate(components):
        for node in component:
            color_map[node] = i

    # Pripravimo seznam barv za vozlišča
    node_colors = [color_map[node] for node in G.nodes()]

    #draw_graph(G, "Vizualizacija povezanih komponent v grafu", node_color="lightblue", with_labels=False, node_size=40)
    # Vizualizacija grafa s poudarjenimi komponentami

    # Izpis rezultatov
    print("Število vozlišč:", num_nodes)
    print("Število povezav:", num_edges)
    print("Število vozlišč v največji WCC:", num_nodes_wcc)
    print("Število povezav v največji WCC:", num_edges_wcc)
    print("Število vozlišč v največji SCC:", num_nodes_scc)
    print("Število povezav v največji SCC:", num_edges_scc)
    print("Povprečni koeficient gručenja:", avg_clustering)
    print("Diameter:", graph_diameter)
    print("Število povezanih komponent:", num_components)