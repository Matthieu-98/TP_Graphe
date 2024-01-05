import networkx as nx
import matplotlib.pyplot as plt

# ------------- figure ------------- 1

nodes1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

G1 = nx.Graph()
G1.add_nodes_from(nodes1)
G1.add_edges_from([(1, 2), (1, 4), (2, 3), (2, 5), (3, 6), (4, 5), (4, 7), (5, 6), (5, 8), (6, 9), (7, 8), (8, 9), (9, 8)])

pos1 = nx.spring_layout(G1)
nx.draw(G1, pos1, with_labels=True, node_size=220, node_color='blue', font_weight='bold')
labels = nx.get_node_attributes(G1, 'pos1')
nx.draw_networkx_labels(G1, 'pos1', labels=labels)

# ------------- figure ------------- 2
position = {
    1: (0.5, 1),
    2: (0, 0.5),
    3: (1, 0.5),
    4: (0, 0),
    5: (1, 0),
    6: (0.5, -0.5)
}

nodes2 = [1, 2, 3, 4, 5, 6]
G2 = nx.Graph()
G2.add_nodes_from(nodes2)
G2.add_edges_from([(1, 4), (1, 5), (4, 5), (2, 3), (3, 6), (2, 6)])

pos2 = position
plt.figure(figsize=(8, 5))
nx.draw(G2, pos2, with_labels=True, node_size=100, node_color='green')


plt.title("Exercice 2")
plt.show()
