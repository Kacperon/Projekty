# 1. Wykonujemy DFS, "usuwając" na bieżąco odwiedzane krawędzie i nie zabraniając wielokrotnego wejścia do
# tego samego wierzchołka
# 2. Po przetworzeniu wierzchołka dodajemy go na początek tworzonego cyklu.

# Usuwanie krawędzi (poprzez zerowanie w macierzy)

# Na macierzy sąsiedztwa.
# Załóżmy, że spójny.

from collections import deque

def EulerCycle(G):
    n = len(G)
    euler =[]
    
    def EulerVisit(G, u):
        for v in range(n):
            if G[u][v] > 0:
                G[u][v], G[v][u] = 0, 0
                EulerVisit(G, v)

                euler.append(u)
    
    euler.append(0)
    EulerVisit(G, 0) # bez fora bo to cykl (i graf nieskierowany)

    return euler

G = [
    [0, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 1, 0],
    [0, 1, 0, 1, 0, 0],
    [0, 1, 1, 0, 1, 1],
    [1, 1, 0, 1, 0, 1],
    [0, 0, 0, 1, 1, 0]
]

print(EulerCycle(G))




