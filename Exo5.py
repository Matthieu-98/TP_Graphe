import networkx as nx
import matplotlib.pyplot as plt
from numpy import array

G = nx.Graph()

# ----------- Gestion-des-sommets ----------

G.add_node(0, label='A', col='pink')
G.add_node(1, label='B', col='red')
G.add_node(2, label='C', col='white')
G.add_node(3, label='D', col='white')
G.add_node(4, label='E', col='white')
G.add_node(5, label='F', col='blue')

# ----------- Gestion-des-arrêtes ----------

G.add_edge(0, 1, weight=6)
G.add_edge(0, 2, weight=5)
G.add_edge(0, 4, weight=1)
G.add_edge(4, 1, weight=5)
G.add_edge(4, 2, weight=1)
G.add_edge(4, 3, weight=3)
G.add_edge(2, 3, weight=8)
G.add_edge(4, 5, weight=6)
G.add_edge(3, 5, weight=9)


# ------colorer------les------noeuds-----

liste = list(G.nodes(data='col'))
colorNodes = {}
for noeud in liste:
    colorNodes[noeud[0]] = noeud[1]
print(colorNodes)

# ------coloriage----des------noeuds------

colorList = [colorNodes[node] for node in colorNodes]
print(colorList)

# -----étiquetages----des----noeuds-------

liste = list(G.nodes(data='label'))
labels_Nodes = {}
for noeud in liste:
    labels_Nodes[noeud[0]] = noeud[1]
print(labels_Nodes)


# ------Traitement-----des----sommets----

labels_edges = {}
labels_edges = {edge: G.edges[edge]['weight'] for edge in G.edges}
print(labels_edges)

# ------Représentation---du---graphe-----

pos = nx.spring_layout(G)
plt.figure(figsize=(6, 4))
nx.draw(G, pos, with_labels=True, node_size=500, font_weight='bold')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels_edges, font_color='red')
plt.show()
