import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd        
import numpy as np 

print("\n\n\n")

print("Dane przedstawiają, którzy studenci, zapisali się na jakies kursy, lub kurs.")
print("/n")
print("Student może zapisać się na jeden lub, więcej kursów, ale naturalnie student nie ma połączenia ze studentem, jak i kurs z kursem.")
print("/n")
print("Jest 100 studentów i 50 kursów.")

# PIERWSZY WIDOK 

# Ścieżka do pliku CSV
sciezka = "your_path.csv"

dane = pd.read_csv(sciezka)

B = nx.Graph()
students = dane['Student'].unique()
courses = dane['Kurs'].unique()

B.add_nodes_from(students, bipartite=0)  # Grupa 1 (studenci)
B.add_nodes_from(courses, bipartite=1)  # Grupa 2 (kursy)

edges = list(zip(dane['Student'], dane['Kurs']))
B.add_edges_from(edges)

pos = nx.drawing.layout.bipartite_layout(B, students)

plt.figure(figsize=(12, 8))
nx.draw(
    B, pos,
    with_labels=True,
    node_color=["skyblue" if node in students else "lightgreen" for node in B.nodes()],
    edge_color="lightblue",
    node_size=800,
    font_size=8
)
plt.title("Graf dwudzielny: Studenci - Kursy", fontsize=14)
plt.show()

# DRUGI WIDOK

B = nx.Graph()
with open(sciezka) as f:
    for line in f:
        u, v = line.strip().split(',')
        B.add_edge(u, v)

for component in nx.connected_components(B):
    subgraph = B.subgraph(component)
    if nx.is_bipartite(subgraph):
        v1, v2 = nx.bipartite.sets(subgraph)
        nx.set_node_attributes(B, {node: 0 for node in v1}, "bipartite")
        nx.set_node_attributes(B, {node: 1 for node in v2}, "bipartite")

students = {n for n, d in B.nodes(data=True) if d["bipartite"] == 0}
courses = {n for n, d in B.nodes(data=True) if d["bipartite"] == 1}

# Tworzenie macierzy sąsiedztwa
adj_matrix = nx.bipartite.biadjacency_matrix(B, row_order=students, column_order=courses).toarray()

# Przygotowanie macierzy pełnej z blokami (zerowa wokół A(1,2))
full_matrix = np.zeros((len(students) + len(courses), len(students) + len(courses)))
full_matrix[:len(students), len(students):] = adj_matrix  # A(1,2)
full_matrix[len(students):, :len(students)] = adj_matrix.T  # A(2,1)

# Rysowanie macierzy sąsiedztwa
plt.figure(figsize=(8, 8))
plt.imshow(full_matrix, cmap="Greys", interpolation="nearest")
plt.title("Macierz sąsiedztwa grafu dwudzielnego")
plt.xlabel("Wierzchołki (studenci + kursy)")
plt.ylabel("Wierzchołki (studenci + kursy)")

# Dodanie linii oddzielających 4 komórki

rows, cols = len(students), len(courses)
plt.axhline(y=rows - 0.5, color='black', linewidth=0.5)  # Linia pozioma
plt.axvline(x=rows - 0.5, color='black', linewidth=0.5)  # Linia pionowa

plt.show()


