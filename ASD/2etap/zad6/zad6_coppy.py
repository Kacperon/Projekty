from zad6testy import runtests

from queue import PriorityQueue
def dijkstra(G,G_2,s,e):
    n = len(G)
    distance = [float("inf") for _ in range(n)]
    distance_2 = [float("inf") for _ in range(n)]
    distance[s] = 0
    distance_2[s] = 0

    Q=PriorityQueue()
    Q.put((0,s,True))

    while not Q.empty():
        
        (cur_distance, v, flag) = Q.get()
        if v==e: return cur_distance

        if cur_distance > distance[v]: continue
        
        for v_son, weight in G[v]:
            dist = cur_distance + weight

            if dist < distance[v_son]:
                distance[v_son] = dist
                Q.put((dist, v_son,True))
        if flag:
            for v_son, weight in G_2[v]:
                dist = cur_distance + weight

                if dist < distance_2[v_son]:
                    distance_2[v_son] = dist
                    Q.put((dist, v_son,False))
    return distance[e]

def jumper(G, s, w ):

    n=len(G[0])
    G_son=[[]for _ in range(n)]
    G_son_2=[[]for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if G[i][j]:
                G_son[i].append((j,G[i][j]))
                # for k in range(n):
                #     if G[j][k] and i!=k:
                #         if G[i][j]>G[j][k]:
                #             distance=G[i][j]
                #         else:distance=G[j][k]
                #         G_son_2[i].append((k,distance))
    for v,i in enumerate(G_son):
        for j in i:
            d = [float('inf')] * n
            for k in G_son[j[0]]:
                if k[0]!=v:
                    if j[1]>k[1]:
                        distance=j[1]
                    else: distance=k[1]
                    if d[k[0]]>distance:
                        d[k[0]]=distance
                        G_son_2[v].append((k[0],distance))
    # tu prosze wpisac wlasna implementacje
    wynik=dijkstra(G_son,G_son_2,s,w)
    return wynik

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( jumper, all_tests = True )