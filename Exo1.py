import networkx as nx
import matplotlib.pyplot as plt


nodes = [1, 2, 3, 4, 5]

#-----Graphe-non-orienté----#

G = nx.Graph()
G.add_nodes_from(nodes)
G.remove_node(1)

G.add_edges_from([(2, 3), (2, 5), (3, 4), (4, 5)])

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=500, node_color='darkblue', font_weight='bold')

labels = nx.get_node_attributes(G, 'pos')
nx.draw_networkx_labels(G, 'pos', labels=labels)

#-----Graphe-orienté--------#

DG = nx.DiGraph()
DG.add_nodes_from(nodes)
DG.add_edges_from([(1, 3), (2, 3), (2, 4), (2, 5), (4, 5), (5, 1)])

pos2 = nx.spring_layout(DG)
nx.draw(DG, pos2, with_labels=True, node_size=500, node_color='blue', font_weight='bold')

labels = nx.get_node_attributes(DG, 'pos2')
nx.draw_networkx_labels(DG, 'pos2', labels=labels)

plt.title("Exercice 1")
plt.show()
