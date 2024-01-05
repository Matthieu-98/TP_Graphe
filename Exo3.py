import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from random import randint

G = nx.Graph()
nodes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
G.add_nodes_from(nodes)

edges = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (10, 11), (11, 12), (12, 13), (13, 14), (14, 15)]
edges_to_get = 15
aleatory_edges = edges[:randint(1, edges_to_get)]

G.add_edges_from(aleatory_edges)

nx.draw(G, with_labels=True, font_weight='bold', node_size=200, node_color='silver', edge_color='gold')
plt.show()
