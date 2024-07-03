#Kacper Feliks
#mój alborytm to algorytm dijkstry puszczony v razy dla każdego wieżchołka który ma rower przesiadamy się na rower
#i uruchamiamy algorytm dijkstry z nową prądkością
#O(VElogV)
from egz1atesty import runtests
from queue import PriorityQueue

def dijkstra(G, s, e):
    n = len(G)
    D = [float("inf") for _ in range(n)]
    D[s] = 0
    Q = PriorityQueue()

    
    Q.put((0, s))

    while not Q.empty():

        (cur_distance, v) = Q.get()

        if cur_distance > D[v]: continue

        for v_son, weight in G[v]:
            dist = cur_distance + weight

            if dist < D[v_son]:
                D[v_son] = dist
                Q.put((dist, v_son))
        
    return D

def rower(G, s, e, speed):
    n = len(G)
    D = [float("inf") for _ in range(n)]
    D[s] = 0
    Q = PriorityQueue()

    
    Q.put((0, s))

    while not Q.empty():

        (cur_distance, v) = Q.get()

        if cur_distance > D[v]: continue

        for v_son, weight in G[v]:
            dist = cur_distance + (weight*speed)

            if dist < D[v_son]:
                D[v_son] = dist
                Q.put((dist, v_son))
        
    return D[e]





def armstrong( B, G, s, t):
  e=len(G)
  n=0
  for i in range(e):
      n=max(n,G[i][0],G[i][1])
  n+=1
  G_son=[[]for i in range(n)]
  for i in G:
      G_son[i[0]].append((i[1],i[2]))
      G_son[i[1]].append((i[0],i[2]))

  B_son=[-1 for i in range(n)]
  for i in B:
      if B_son[i[0]]>i[1]/i[2] or B_son[i[0]]==-1:
        B_son[i[0]]=i[1]/i[2]
      
  D=dijkstra(G_son,s,t)
  mini=D[t]
  for i in range(n):
      if B_son[i]!=-1 and B_son[i]<1:

        curent=rower(G_son,i,t,B_son[i])+D[i]
        mini=min(mini,curent)

  return int(mini//1)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( armstrong, all_tests = True )
