from zad6testy import runtests
# Imię i nazwisko studenta: [Twoje imię i nazwisko]

# Algorytm znajdowania najkrótszej ścieżki w grafie z użyciem "dwumilowych butów"
# Złożoność czasowa: O(V^2 * log(V) + E)
# Złożoność pamięciowa: O(V^2)
from heapq import heappop, heappush
from collections import defaultdict

def jumper(G, s, w):
    n = len(G)
    
    # Tworzenie tablicy odległości: dist[v][0] - zwykła krawędź, dist[v][1] - po dwumilowych butach
    dist = [[float('inf')] * 2 for _ in range(n)]
    dist[s][0] = 0
    
    # Kolejka priorytetowa (waga, wierzchołek, stan 0/1)
    pq = [(0, s, 0)]
    
    while pq:
        d, u, state = heappop(pq)
        
        # Jeśli już znaleziono krótszą ścieżkę, pomijamy
        if d > dist[u][state]:
            continue
        
        for v in range(n):
            if G[u][v] > 0:
                # Przejście zwykłą krawędzią
                if state == 0 and d + G[u][v] < dist[v][0]:
                    dist[v][0] = d + G[u][v]
                    heappush(pq, (dist[v][0], v, 0))
                # Przejście dwumilowymi butami
                if state == 0:
                    for k in range(n):
                        if G[v][k] > 0 and k != u and d + max(G[u][v], G[v][k]) < dist[k][1]:
                            dist[k][1] = d + max(G[u][v], G[v][k])
                            heappush(pq, (dist[k][1], k, 1))
                # Przejście zwykłą krawędzią po dwumilowych butach
                if state == 1 and d + G[u][v] < dist[v][0]:
                    dist[v][0] = d + G[u][v]
                    heappush(pq, (dist[v][0], v, 0))
    
    return min(dist[w][0], dist[w][1])


runtests( jumper, all_tests = True )
