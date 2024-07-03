from zad5testy import runtests
from math import inf
from queue import PriorityQueue

def dijkstra(G,s,e,G_S,S):
    n=len(G)
    distance=[float("inf")]*n
    distance[s]=0

    Q=PriorityQueue()
    Q.put((0,s))
    flag=True
    while not Q.empty():
        
        cur_distance, v = Q.get()
        if flag and G_S[v]:
            flag = False
            for i in S:
                if i!=v:
                    Q.put((cur_distance,i))
                    distance[i]=cur_distance
        if cur_distance > distance[v]: continue

        for v_son, weight in G[v]:
            dist = cur_distance + weight

            if dist < distance[v_son]:
                distance[v_son] = dist
                Q.put((dist, v_son))
    return distance[e]




def spacetravel( n, E, S, a, b ):
    if b==2:
        print("")
    n = max(max(u[1] for u in E), a, b) + 1
    G = [[]for _ in range(n+1)]
    for u,v,w in E:
        G[u].append((v,w))
        G[v].append((u,w))

    G_S=[False]*n
    for i in S: G_S[i]=True

    time =dijkstra(G,a,b,G_S,S)

    return time if time!=float("inf") else None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )