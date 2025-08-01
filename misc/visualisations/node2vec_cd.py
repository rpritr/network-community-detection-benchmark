from node2vec import Node2Vec
import networkx as nx

# 1. Ustvari preprost graf
G = nx.karate_club_graph()

# 2. Ustvari Node2Vec model
node2vec = Node2Vec(G, dimensions=2, walk_length=10, num_walks=50, workers=1)

# 3. Učenje vektorjev
model = node2vec.fit(window=5, min_count=1)

# 4. Dobimo vektor za vozlišče 0
vec_0 = model.wv['0']
print("Vektor za vozlišče 0:", vec_0)

# 5. Poišči podobna vozlišča
print("Najbolj podobna vozlišča vozlišču 0:")
print(model.wv.most_similar('0'))