from zad5testy import runtests
from math import inf
from queue import PriorityQueue

def dijkstra(G,s,e):
    n=len(G)
    distance=[float("inf")]*n
    visited=[False]*n
    distance[s]=0

    Q=PriorityQueue()
    Q.put((0,s))

    while not Q.empty():
        
        cur_distance, v=Q.get()

        if cur_distance > distance[v]: continue

        for v_son, weight in G[v]:
            dist = cur_distance + weight

            if not visited[v_son] and dist < distance[v_son]:
                distance[v_son]=dist
                Q.put((dist, v_son))
        visited[v]=True
    return distance[e]

def dijkstra2(G,G_S,s):
    n=len(G)
    distance=[float("inf")]*n
    visited=[False]*n
    distance[s]=0
    dist_min=float("inf")
    Q=PriorityQueue()
    Q.put((0,s))

    while not Q.empty():
        
        cur_distance, v=Q.get()
        if G_S[v]:
            dist_min=min(cur_distance,dist_min)
        if cur_distance > distance[v]: continue

        for v_son, weight in G[v]:
            dist = cur_distance + weight

            if not visited[v_son] and dist < distance[v_son]:
                distance[v_son]=dist
                if G_S[v_son]:
                    dist_min=min(dist,dist_min)
                Q.put((dist, v_son))
        visited[v]=True
    return dist_min


def spacetravel( n, E, S, a, b ):
    n = max(max(u[1] for u in E), a, b) + 1
    G = [[]for _ in range(n+1)]
    for u,v,w in E:
        G[u].append((v,w))
        G[v].append((u,w))
    G_S=[False]*n
    for i in S: G_S[i]=True

    time=min(dijkstra(G,a,b), dijkstra2(G,G_S,a)+dijkstra2(G,G_S,b))

    return time if time!=float("inf") else None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )