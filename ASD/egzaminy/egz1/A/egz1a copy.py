#Kacper Feliks
#mój algorytm działa w 2 etapach 
#na początku używa zwykłego algorytmu dijkstry na całym grafie
#następnie uruchamia ten sam algorytm z założeniem że zawsze przesiada się na rower
#i zwraca wartość minimalną z obu opcji

#O(ElogV)
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

def rower(G, s, e, D, B):
    n = len(G)
    SP=[float("inf") for _ in range(n)]
    Q = PriorityQueue()
    
    for i in B:
        Q.put((D[i[0]],i[0],i[1]/i[2]))

    

    while not Q.empty():

        (cur_distance, v,speed) = Q.get()

        if cur_distance > D[v] and SP[v]>speed: continue

        for v_son, weight in G[v]:
            dist = cur_distance + (weight*speed)

            if dist < D[v_son]:
                D[v_son] = dist
                SP[v] = speed
                Q.put((dist, v_son,speed))
            if SP[v]>speed:
               SP[v] = speed
               Q.put((dist, v_son,speed))

        
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
      
  D=dijkstra(G_son,s,t)
  mini=rower(G_son,s,t,D,B)
  
  

  return int(mini//1)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( armstrong, all_tests = True )
