import networkx as nx
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pyvis.network import Network


sciezka = "your_path.csv"
G = nx.Graph()

with open(sciezka) as r:
    for line in r:
        u, v = line.split(' ')
        try:
            G.add_edge(int(u), int(v))
        except:
            pass
print(f"Liczba wierzchołków: {G.number_of_nodes()}")
print(f"Liczba krawędzi: {G.number_of_edges()}")


plt.figure(figsize=(10, 8))
nx.draw(G, with_labels=True, node_color="lightblue", font_size=8, node_size=500, edge_color="gray")
plt.title("Wizualizacja grafu")
plt.show()

adjacency_matrix = nx.adjacency_matrix(G).toarray()

incidence_matrix = nx.incidence_matrix(G).toarray()

plt.imshow(adjacency_matrix, cmap='viridis')
plt.colorbar()
plt.title("Macierz sasiedztwa")
plt.show()

plt.imshow(incidence_matrix, cmap ='viridis')
plt.colorbar()
plt.title("Maicerz incydencji")
plt.show()

G_adj = nx.from_numpy_array(adjacency_matrix)

plt.figure(figsize=(8, 6))
nx.draw(G_adj, with_labels=True, node_color="skyblue", node_size=700, edge_color="gray", font_size=10)
plt.title("Graf z macierzy sąsiedztwa")
plt.show()

rows, cols = np.where(incidence_matrix == 1)
edges = list(zip(rows[::2], rows[1::2])) 

G_inc = nx.Graph()
G_inc.add_edges_from(edges)

plt.figure(figsize=(8, 6))
nx.draw(G_inc, with_labels=True, node_color="lightgreen", node_size=700, edge_color="gray", font_size=10)
plt.title("Graf z macierzy incydencji")
plt.show()

net = Network()
net.from_nx(G_adj)
net.toggle_physics(False)
net.save_graph("sasiedztwa.html")

G_inc = nx.relabel_nodes(G_inc, lambda x: int(x))
net = Network()
net.from_nx(G_inc)
net.toggle_physics(False)
net.save_graph("incydencji.html")


# Jezeli w macierzy sasiedztwa, '1' wystepuja glownie na przekatnej, oznacza to, ze mamy prawdopodobnie doczynienia z grafem pelnym, być może klikami.

