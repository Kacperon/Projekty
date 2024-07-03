from egz1atesty import runtests
from queue import PriorityQueue

def dijkstra(G, B, s, e):
    n = len(G)
    D = [float("inf") for _ in range(n)]
    D_r = [float("inf") for _ in range(n)]
    D_speed=[-1 for _ in range(n)]
    D[s] = 0
    Q = PriorityQueue()
    if B[0]!=-1:
        D_r[s]=0
        Q.put((0, s, B[0]))

    
    Q.put((0, s, -1))

    while not Q.empty():

        (cur_distance, v, speed) = Q.get()

        if cur_distance > D[v] and speed==-1: continue
        if speed==-1:
            for v_son, weight in G[v]:
                dist = cur_distance + weight

                if dist < D[v_son]:
                    D[v_son] = dist
                    Q.put((dist, v_son,-1))
                    if B[v_son]!=-1:
                        Q.put((dist,v_son,B[v_son]))
        if cur_distance > D_r[v] and speed!=-1: continue
        if speed!=-1:
            for v_son, weight in G[v]:
                dist = cur_distance + (weight*speed)
                if dist < D_r[v_son]:
                    D_r[v_son] = dist
                    D_speed[v_son] = speed
                    Q.put((dist,v_son,speed))
                if speed>D_speed[v_son]:
                    Q.put((dist,v_son,speed))


            
        
    return int(min(D[e],D_r[e])//1)

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
      if B_son[i[0]]<i[1]/i[2]:
        B_son[i[0]]=i[1]/i[2]
      
  

  return dijkstra(G_son,B_son,s,t)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( armstrong, all_tests = True )
