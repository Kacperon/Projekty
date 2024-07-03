INF = float('inf')

def floyd_warshall(graph):
    # Inicjalizacja macierzy odległości
    dist = [[INF for _ in range(len(graph))] for _ in range(len(graph))]
    
    # Wypełnienie macierzy odległości danymi z grafu
    for i in range(len(graph)):
        for j in range(len(graph)):
            if i == j:
                dist[i][j] = 0
            elif graph[i][j] != 0:
                dist[i][j] = graph[i][j]
    
    # Algorytm Floyd-Warshalla
    for k in range(len(graph)):
        for i in range(len(graph)):
            for j in range(len(graph)):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    return dist

# Przykładowy graf w postaci macierzy sąsiedztwa
graph = [
    [0, 3, 0, 7],
    [8, 0, 2, 0],
    [5, 0, 0, 1],
    [2, 0, 0, 0]
]


result = floyd_warshall(graph)
for row in result: print(row)



def bellman_ford(G, src):
    V = len(G)
    dist = [float("inf")] * V
    dist[src] = 0

    for _ in range(V - 1):
        for u in range(V):
            for v, weight in G[u]:
                if dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight

    # Sprawdzenie na obecność cyklu o ujemnej wadze
    for u in range(V):
        for v, weight in G[u]:
            if dist[u] + weight < dist[v]:
                print("Graf zawiera cykl o ujemnej wadze")
                return

    print("Wierzchołek  Odległość od źródła")
    for i in range(V):
        print("{0}\t\t{1}".format(i, dist[i]))


# Przykład użycia:
G = [
    [(1, 1)],#0
    [(2, 1)],#1
    [(3, 1),(4,-2)],#2
    [],#3
    [(1,1)],#4
]

bellman_ford(G, 0)

