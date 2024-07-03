from zad5testy import runtests
from math import inf
from queue import PriorityQueue
import heapq as h
def Dijkstra_list(G, s, k):

    n=len(G)
    distance = [ inf for _ in range(n) ]
    parent = [None for _ in range(n)]
    visited = [False for _ in range(n)]
    distance[s] = 0

    # PQ = PriorityQueue()
    # PQ.put((0, s))
    PQ=[]
    h.heappush(PQ,(0,s))

    # while not PQ.empty():
    while len(PQ):

        # current_distance, vertex = PQ.get()                             # 1. ściągam z kolejki element o najmniejszej odległości
        current_distance, vertex = h.heappop(PQ)
        if current_distance > distance[vertex]: continue                # sprawdzenie, cczy odleglosc z jaka dodano go do kolejki (bo 
                                                                        # moze byc dodany kilka razy zanim zostanie przetworzony) jest 
                                                                        # mniejsza od juz wpisanej najkrotszej sciezki

        for neighbour, weight in G[vertex]:                             # 2. Sprawdzam sąsiadów
            dist = current_distance + weight

            if dist < distance[neighbour] and not visited[neighbour]:   # Jeśli nie był juz wczesniej przeglądnięty, a odległość z
                distance[neighbour] = dist                              # aktualnego jest mniejsza niz wczesniej wpisana- aktualizuje 
                parent[neighbour] = vertex                              # odleglosc, zmieniam parenta i dodaje go do kolejki
                # PQ.put((dist, neighbour))
                h.heappush(PQ,(dist, neighbour))
        visited[vertex] = True  
    if distance[k]==inf:
        return None                            # bo przeglądnięci są wszyscy jego sąsiedzi
    return distance[k]


def spacetravel( n, E, S, a, b ):
    n = max(max(u[1] for u in E), a, b) + 1
    G = [[]for _ in range(n+1)]
    for u,v,w in E:
        G[u].append((v,w))
        G[v].append((u,w))
    for i in S:
        G[n].append((i,0))
        G[i].append((n,0))
    czas=Dijkstra_list(G,a,b)
    return czas

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )