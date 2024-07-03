from math import inf
from queue import PriorityQueue

# O( ( E + V )logV )
def Dijkstra_list(G, s):

    n=len(G)
    distance = [ inf for _ in range(n) ]
    parent = [None for _ in range(n)]
    visited = [False for _ in range(n)]
    distance[s] = 0

    PQ = PriorityQueue()
    PQ.put((0, s))

    while not PQ.empty():

        current_distance, vertex = PQ.get()                             # 1. ściągam z kolejki element o najmniejszej odległości

        if current_distance > distance[vertex]: continue                # sprawdzenie, cczy odleglosc z jaka dodano go do kolejki (bo 
                                                                        # moze byc dodany kilka razy zanim zostanie przetworzony) jest 
                                                                        # mniejsza od juz wpisanej najkrotszej sciezki

        for neighbour, weight in G[vertex]:                             # 2. Sprawdzam sąsiadów
            dist = current_distance + weight

            if dist < distance[neighbour] and not visited[neighbour]:   # Jeśli nie był juz wczesniej przeglądnięty, a odległość z
                distance[neighbour] = dist                              # aktualnego jest mniejsza niz wczesniej wpisana- aktualizuje 
                parent[neighbour] = vertex                              # odleglosc, zmieniam parenta i dodaje go do kolejki
                PQ.put((dist, neighbour))

        visited[vertex] = True                                          # bo przeglądnięci są wszyscy jego sąsiedzi

    print("distance from ", s, ": ")
    print(distance)
    print("parents: ")
    print(parent)
    
# O( V^2 )
def Dijkstra_matrix(G, s):
    distance = [ inf for _ in range(len(G)) ]
    visited = [ False for _ in range(len(G)) ]
    parent = [None for _ in range(len(G))]
    distance[s] = 0

    while True:
        shortest_distance = inf
        shortest_index = -1
        for i in range(len(G)):
            if distance[i] < shortest_distance and not visited[i]:
                shortest_distance = distance[i]
                shortest_index = i
        
        if shortest_index == -1:
            print("distance from ", s, ": ")
            print(distance)
            print("parents: ")
            print(parent)
            return 0
        
        for i in range(len(G[shortest_index])):
            if G[shortest_index][i] != 0 and (distance[i] > (distance[shortest_index] + G[shortest_index][i])):
                distance[i] = distance[shortest_index] + G[shortest_index][i]
                parent[i] = shortest_index
        
        visited[shortest_index] = True






G = [[(1,1), (7,2)],
     [(2,2), (0,1), (4,3)],
     [(1,2), (3,5)],
     [(2,5), (4,2), (6,1)],
     [(1,3), (3,2), (7,1), (5,3)],
     [(4,3), (6,8), (8,1)],
     [(3,1), (5,8), (8,4)],
     [(0,2), (4,1), (8,7)],
     [(7,7), (5,1), (6,4)]]

Dijkstra_list(G, 0)