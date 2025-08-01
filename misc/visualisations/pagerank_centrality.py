import networkx as nx
import matplotlib.pyplot as plt

# Ustvari usmerjen graf
G = nx.erdos_renyi_graph(8,0.25, directed=True)


# Izračunaj PageRank centralnost
pagerank = nx.pagerank(G, alpha=0.85)

# Postavitev vozlišč
pos = nx.spring_layout(G, seed=42)


nx.draw_networkx_nodes(
    G, pos,
    node_color='white',
    edgecolors='black',
    linewidths=2,
    node_size=500
)

# Nariši povezave
nx.draw_networkx_edges(
    G, pos,
    edge_color='black',
    arrows=True
)

# Oznake vozlišč
nx.draw_networkx_labels(
    G, pos,
    font_color='black',
    font_size=10
)

# Prikaži PageRank vrednosti ob vozliščih
for node, (x, y) in pos.items():
    plt.text(
        x + 0.05, y + 0.05,
        f"PR={pagerank[node]:.2f}",
        fontsize=8,
        color='red'
    )

plt.title("Usmerjen graf z PageRank centralnostjo")
plt.axis('off')
plt.show()