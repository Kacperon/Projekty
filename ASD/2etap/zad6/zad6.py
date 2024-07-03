#Kacper Feliks
#mój algorytm tworzy 2 grafy listy sąsiedstwa jedną skoku o 1 i drugą skoku o 2 z najmniejszą wagą
#następnie uruchamia algorytm dijkstry przerobiony do posiadania 2 list distance aby uwzgldniać możliwość skoku,
#złożoność tworzenia list skoku o 1 i o 2 to O(V^2+VE)
#złożoność dijkstry to O(ElogV)
#co daje złożoność czasową O(V^2+VE)
#i pamięciową O(EV)

from zad6testy import runtests
import heapq as h

def dijkstra(G,G_2,s,e):
    n = len(G)
    distance = [float("inf") for _ in range(n)]
    distance_2 = [float("inf") for _ in range(n)]
    distance[s] = 0
    distance_2[s] = 0

    PQ=[]
    h.heappush(PQ,(0,s,True))

    while len(PQ):
        
        (cur_distance, v, flag) = h.heappop(PQ)
        if v==e: return cur_distance

        if cur_distance > distance[v]: continue
        
        for v_son, weight in G[v]:
            dist = cur_distance + weight

            if dist < distance[v_son]:
                distance[v_son] = dist
                h.heappush(PQ,(dist, v_son,True))
        if flag:
            for v_son, weight in G_2[v]:
                dist = cur_distance + weight

                if dist < distance_2[v_son]:
                    distance_2[v_son] = dist
                    h.heappush(PQ,(dist, v_son,False))
    return distance[e]

def jumper(G, s, w ):

    n=len(G[0])
    G_son=[[]for _ in range(n)]
    G_son_2=[[]for _ in range(n)]
    for i in range(n):#tworzenie listy sąsiedstwa
        for j in range(n):
            if G[i][j]:
                G_son[i].append((j,G[i][j]))

    for v,i in enumerate(G_son): #twozenie listy sąsiedstwa użycia butów
        d = [float('inf')] * n #użycie distance żeby uniknąć 2 krawędzi o różnych wagach
        for j in i:
            for k in G_son[j[0]]:
                if k[0]!=v:
                    if j[1]>k[1]:
                        distance=j[1]
                    else: distance=k[1]
                    if d[k[0]]>distance:
                        d[k[0]]=distance
        for k,d in enumerate(d):
            G_son_2[v].append((k,d))

    return dijkstra(G_son,G_son_2,s,w)


runtests( jumper, all_tests = True )

