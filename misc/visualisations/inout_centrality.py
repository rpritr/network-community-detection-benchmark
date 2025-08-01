import networkx as nx
import matplotlib.pyplot as plt

# Ustvari graf: cikel ali zvezda
G = nx.erdos_renyi_graph(7,0.33, directed=True)
# G = nx.star_graph(5)

# Izračun closeness centrality
closeness_in = nx.in_degree_centrality(G)
closeness_out = nx.out_degree_centrality(G)

# Postavitev vozlišč
pos = nx.spring_layout(G, seed=42)

# Nariši vozlišča in povezave
nx.draw_networkx_nodes(
    G, pos,
    node_color='white',
    edgecolors='black',
    linewidths=2,
    node_size=500
)

nx.draw_networkx_edges(
    G, pos,
    edge_color='black'
)

# Napiši oznake vozlišč
nx.draw_networkx_labels(
    G, pos,
    font_color='black',
    font_size=10
)

# Dodaj closeness ob strani vozlišča
for node, (x, y) in pos.items():
    plt.text(
        x + 0.05, y + 0.10,
        f"Cin={closeness_in[node]:.2f}",
        fontsize=8,
        color='red'
    )
    plt.text(
        x + 0.05, y+0.05,
        f"Cout={closeness_out[node]:.2f}",
        fontsize=8,
        color='red'
    )
#plt.title("Graf z closeness centrality")
plt.axis('off')
plt.show()