import networkx as nx
import matplotlib.pyplot as plt
import random

# 1. Ustvari naključni graf
G = nx.erdos_renyi_graph(n=10, p=0.3, seed=42)

# 2. Izberi naključno začetno vozlišče
start_node = random.choice(list(G.nodes()))
path = [start_node]

# 3. Izvedi naključno pot dolžine n
walk_length = 7
current_node = start_node

for _ in range(walk_length - 1):
    neighbors = list(G.neighbors(current_node))
    if not neighbors:
        break  # ni več kam naprej
    next_node = random.choice(neighbors)
    path.append(next_node)
    current_node = next_node

# 4. Izriši graf
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_color="lightgray", edge_color="gray")

# Označi pot (rdeče)
path_edges = list(zip(path[:-1], path[1:]))
nx.draw_networkx_nodes(G, pos, nodelist=path, node_color='red')
nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)

# 5. Izpiši pot
print("Naključna pot (random walk):")
print(" -> ".join(map(str, path)))

plt.title("Naključna pot po grafu (Random Walk)")
plt.axis('off')
plt.show()