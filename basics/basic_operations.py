# nodes to ID stron z facebooka, a edges to połączenia między stronami (polubienie stron)
# np. 0,18427 --- strona o ID 0, polubiła strone o ID 18427

import networkx as nx

sciezka = "your_path.csv"
G = nx.Graph()

with open(sciezka) as r:
    for line in r:
        u, v = line.split(',')
        try:
            G.add_edge(int(u), int(v))
        except:
            pass

# print(f"Liczba wierzchołków: {G.number_of_nodes()}")
# print(f"Liczba krawędzi: {G.number_of_edges()}")

def znajdz_najkrotsza_sciezke(G, start, end):
    try:
        sciezka = nx.shortest_path(G, source=start, target=end)
        print(f"Najkrótsza ścieżka od {start} do {end}: {sciezka}")
    except nx.NetworkXNoPath:
        print(f"Brak ścieżki pomiędzy {start} a {end}.")

start = int(input("Podaj ID wierzchołka początkowego: "))
end = int(input("Podaj ID wierzchołka końcowego: "))
znajdz_najkrotsza_sciezke(G, start, end)


if nx.is_eulerian(G):
    sciezka_eulerowska = list(nx.eulerian_path(G))
    print(f"Graf jest eulerowski. Ścieżka eulerowska: {sciezka_eulerowska}")
else:
    print("Graf nie jest eulerowski.")


sciezka = "C:/Users/grzeg/Desktop/rzeczy/SEMESTR_5/SIECI/musae_facebook_edges.csv"
G = nx.DiGraph()  

with open(sciezka) as r:
    for line in r:
        u, v = line.split(',')
        try:
            u, v = int(u), int(v)
            roznica = abs(u - v)  
            if roznica == 0:
                pojemnosc = 100 
            elif roznica < 100:
                pojemnosc = 80
            elif roznica < 600:
                pojemnosc = 50  
            elif roznica < 1200:
                pojemnosc = 30 
            elif roznica < 2000:  
                pojemnosc = 10
            else:
                pojemnosc = 1 
            G.add_edge(u, v, capacity=pojemnosc)
        except :
            pass  

start = int(input("Podaj ID wierzchołka początkowego: "))
end = int(input("Podaj ID wierzchołka końcowego: "))

flow_value, _ = nx.maximum_flow(G, start, end)

print(f"Maksymalny przepływ od {start} do {end}: {flow_value}")