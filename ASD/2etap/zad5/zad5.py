#Kacper Feliks
#Mój program przepisuje graf E do listy sąsiedstwa G posiadającej n+1 wierzchołków
#następnie do wierzchołków z listy S dodaje krawędzie o wadze 0 do wierzchołka o numerze n+1
#i uruchamia algorytm dijkstry z wykorzysstaniem kopca z biblioteki heapq
#na koniec zwraca odległość w grafie G z A do B lub None jak odległość jest nieskończona 
#złożoność mojego algorytmu to O(ElogV) ponieważ tworzenie listy sąsiedstwa jest liniowe
from zad5testy import runtests
import heapq as h

def dijkstra(G,s,e):
    n = len(G)
    distance = [float("inf")]*n
    distance[s] = 0
    PQ=[]
    h.heappush(PQ,(0,s))
    while len(PQ):
        cur_distance, v = h.heappop(PQ)

        if cur_distance > distance[v]: continue

        for v_son, weight in G[v]:
            dist = cur_distance + weight

            if dist < distance[v_son]:
                distance[v_son] = dist
                h.heappush(PQ,(dist, v_son))
    return distance[e]


def spacetravel( n, E, S, a, b ):
    
    G = [[]for _ in range(n+1)]

    for u,v,w in E:
        G[u].append((v,w))
        G[v].append((u,w))

    for i in S:
        G[n].append((i,0))
        G[i].append((n,0))

    time = dijkstra(G,a,b)

    return time if time < float("inf") else None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )