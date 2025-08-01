import networkx as nx
import matplotlib.pyplot as plt

G = nx.star_graph(6)
degrees = dict(G.degree())
pos = nx.spring_layout(G, seed=42)

# vozlišča
nx.draw_networkx_nodes(
    G, pos,
    node_color='white',
    edgecolors='black',
linewidths=2,
    node_size=500
)

# povezave
nx.draw_networkx_edges(G, pos, edge_color='gray')

# oznake vozlišč v VOZLIŠČIH (številke vozlišč)
nx.draw_networkx_labels(
    G, pos,
    font_color='black',    # tukaj nastaviš barvo
    font_size=10,

)

# stopnje ob strani
for node, (x, y) in pos.items():
    plt.text(
        x + 0.10, y + 0.10,
        f"deg={degrees[node]}",
        fontsize=8,
        color='red'
    )

#plt.title("Graf z oznakami vozlišč in njihovimi stopnjami ob strani")
plt.axis('off')
plt.show()