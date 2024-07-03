"""
Program wywołuje BFS na grafie traktując krawędzie o wadze większej niż 1 jako wiele wierzchołków
pośrednich połączonych krawędziami o wadze 1, przechowując dla każdego prawdziwego wierzchołka
najlepszy czas osiągnięty dla każdego poziomu wyczerpania. 
W ten sposób rozważa każdą najkrótszą ścieżkę dla każdego z 17 poziomów wyczerpania dla każdego
z wierzchołków i upewnia się, że Magiczny wojownik nie przekroczy kodeksu :3

Złożoność czasowa: O(E + V)
Złożoność pamięciowa: O(E + V)
"""
from kol2testy import runtests
from collections import deque
from math import inf


class BFSQueue:
    def __init__(self):
        self.queue = deque()

    def is_empty(self):
        return len(self.queue) == 0

    def push(self, v, dist, time_awake, steps_to_v):
        self.queue.append((v, dist, time_awake, steps_to_v))

    def pop(self):
        v, dist, time_awake, steps_to_v = self.queue.popleft()

        # steps_to_v przechowuje informację o tym, przez ile pośrednich wierzchołków trzeba jeszcze
        # przejść aby dostać się do prawdziwego wierzchołka v.
        # Dopóki nie weźmiemy z kolejki prawdziwego (o wartości steps_to_v == 1) wierzchołka, 
        # wkładamy ten wierzchołek o wartości steps_to_v o jeden mniejszej do kolejki
        while steps_to_v > 1:
            self.queue.append((v, dist, time_awake, steps_to_v - 1))
            v, dist, time_awake, steps_to_v = self.queue.popleft()

        return v, dist, time_awake


def modified_bfs(graph, start, end):
    # Przechowujemy najlepsze czasy dla każdego poziomu wyczerpania dla każdego wierzchołka
    bestof = [[inf] * (16+1) for _ in range(len(graph))]
    
    bestof[start] = [0] * (16+1)
    q = BFSQueue()
    q.push(start, 0, 0, 0)

    while not q.is_empty():
        v, dist, time_awake = q.pop()

        if dist > bestof[v][time_awake]: continue

        if v == end: return dist

        for child, path_len in graph[v]:
            new_child_dist = path_len + dist
            child_awake_time = path_len + time_awake
            
            if child_awake_time <= 16 and new_child_dist < bestof[child][child_awake_time]:
                q.push(child, new_child_dist, child_awake_time, path_len)

                bestof[child][child_awake_time] = new_child_dist
                # Eliminowanie potrzeby późniejszego odwiedzania tego wierzchołka gdy
                # odwiedziliśmy go już z lepszym poziomem wyczerpania i czasem
                for i in range(child_awake_time + 1, 16+1):
                    if bestof[child][i] <= new_child_dist: break
                    bestof[child][i] = new_child_dist


                # To samo, ale odpoczywając w docelowym wierzchołku
                if bestof[child][0] > new_child_dist + 8:
                    q.push(child, new_child_dist + 8, 0, path_len + 8)

                    bestof[child][0] = new_child_dist + 8
                    for i in range(1, child_awake_time):
                        if bestof[child][i] <= new_child_dist + 8: break
                        bestof[child][i] = new_child_dist + 8


def warrior(G, s, t):
    graph = [[] for _ in range(max(max(u, v) for u, v, _ in G) + 1)]

    for u, v, w in G:
        graph[u].append((v, w))
        graph[v].append((u, w))

    return modified_bfs(graph, s, t)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( warrior, all_tests = True )

