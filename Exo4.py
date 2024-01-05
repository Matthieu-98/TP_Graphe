import networkx as nx
import matplotlib.pyplot as plt
from numpy import array

# --------Définition-------du--------graphe

G = nx.graph()

# --------Définition-------des-------noeuds

G.add_node(0, label='A', col='pink')    # créé le noeud 0 de nom A et de couleur rose 
G.add_node(1, label='B', col='red')     # créé le noeud 1 de nom B et de couleur rouge 
G.add_node(2, label='C', col='white')   # créé le noeud 2 de nom C et de couleur blanche  
G.add_node(3, label='D', col='white')   # créé le noeud 3 de nom D et de couleur blanche 
G.add_node(4, label='E', col='white')   # créé le noeud 4 de nom E et de couleur blanche 
G.add_node(5, label='F', col='blue')    # créé le noeud 5 de nom F et de couleur bleu 

# --------Définition-------des-------aretes

G.add_edge(0, 1, weight=6)        # crée l'arete reliant les sommets 0 et 1 de poids 6 
G.add_edge(0, 2, weight=5)        # crée l'arete reliant les sommets 0 et 2 de poids 5 
G.add_edge(0, 4, weight=1)        # crée l'arete reliant les sommets 0 et 4 de poids 1 
G.add_edge(4, 1, weight=5)        # crée l'arete reliant les sommets 0 et 1 de poids 5 
G.add_edge(4, 2, weight=1)        # crée l'arete reliant les sommets 0 et 1 de poids 1 
G.add_edge(4, 3, weight=3)        # crée l'arete reliant les sommets 0 et 1 de poids 3 
G.add_edge(2, 3, weight=8)        # crée l'arete reliant les sommets 0 et 1 de poids 8 
G.add_edge(4, 5, weight=6)        # crée l'arete reliant les sommets 0 et 1 de poids 6 
G.add_edge(3, 5, weight=9)        # crée l'arete reliant les sommets 0 et 1 de poids 9 

# ----représentation----du--graphe---basique 

nx.draw(G)      # dessine le graphe
plt.show()      # affiche le graphe




# ------colorer------les------noeuds-----

liste = list(G.nodes(data='col'))   # crée une liste de couleur attribuables pour chaque sommets 
colorNodes = {}        # crée une liste de couleurs vide
for noeud in liste:  # attribue à chaque noeuds sa couleur dans la liste
    colorNodes[noeud[0]] = noeud[1]
print(colorNodes) # affiche les couleurs selon les sommet et leur ordre

# ------coloriage----des------noeuds------

colorList = [colorNodes[node] for node in colorNodes] # convertit colorNodes en liste
print(colorList) # Affiche colorNodes

# -----étiquetages----des----noeuds-------

liste = list(G.nodes(data='label')) # crée une liste de nom attribuables pour chaque sommets
labels_Nodes = {}       # crée une liste de couleurs vide
for noeud in liste:     # attribue à chaque noeuds son nom dans la liste
    labels_Nodes[noeud[0]] = noeud[1]
print(labels_Nodes) # affiche les noms des sommets selon leur ordre


# ------Traitement-----des----sommets----

labels_edges = {} # crée un dictionnaire vide
labels_edges = {edge: G.edges[edge]['weight'] for edge in G.edges} # Remplit le dictionnaire avec comme clé les aretes et comme valeur leur poids
print(labels_edges) # affiches les aretes et leur poids


# ------Représentation---du---graphe-----

pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=700, node_color=colorList, alpha=0.9)
nx.draw_networkx_labels(G, pos, labels=labels_Nodes, with_labels=True, font_size=20, font_color='black', font_family='sans-serif')
nx.draw_networkx_edges(G, pos, width=1)
nx.draw_networkx_edge_labels(G, pos, width=1, edge_labels=labels_edges)
