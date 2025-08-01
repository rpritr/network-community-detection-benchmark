import networkx as nx
import random
import matplotlib.pyplot as plt
from collections import defaultdict

# 1. Ustvari graf z dvema skupnostma
G = nx.Graph()
G.add_edges_from([
    (0, 1), (1, 2), (2, 3), (3, 0),  # Skupnost A
    (4, 5), (5, 6), (6, 7), (7, 4),  # Skupnost B
    (3, 4)  # povezava med skupnostma
])

# 2. Funkcija za slučajni sprehod
def random_walk(G, start, length):
    path = [start]
    current = start
    for _ in range(length):
        neighbors = list(G.neighbors(current))
        if not neighbors:
            break
        current = random.choice(neighbors)
        path.append(current)
    return path

# 3. Izvedi več sprehodov iz vseh vozlišč
walks_by_node = defaultdict(list)
for node in G.nodes():
    for _ in range(10):  # 10 ponovitev
        walk = random_walk(G, node, length=5)
        walks_by_node[node].append(walk)

# 4. Pokaži primer enega sprehoda
example_walk = random_walk(G, start=0, length=10)
print("Primer sprehoda iz vozlišča 0:", example_walk)

# 5. Vizualizacija grafa
pos = nx.spring_layout(G, seed=42)
plt.figure(figsize=(6, 4))
nx.draw(G, pos, with_labels=True, node_color='lightgray', edge_color='gray')
plt.title("Graf za slučajni sprehod")
plt.show()