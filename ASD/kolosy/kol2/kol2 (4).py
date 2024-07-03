#Kacper Feliks

#moj algorytm to przerobiona dijkstra która rozważa każdy wieżchołek z możliwością spania lub nie
#na początku zamienia graf na listę sąsiedstwa
#następnie rozpatruje każdy wieżchołek z możliwościa spania lub nie jak w zwykłej dijkstrze
#jak również wszystkie wieżchołki do których da się dostać z mniejszą ilością nie przespanych godzin niż najkrótrzą ścieżką

#złożonosć O(ElogV) jak dijkstry bo tworzenie listy sąsiedstwa O(E)
from kol2testy import runtests
from queue import PriorityQueue

def dijkstra(G, s, e):
    n = len(G)
    distance = [float("inf") for _ in range(n)]
    distance_sleep = [float("inf") for _ in range(n)]
    distance_not_sleep= [float("inf") for _ in range(n)]
    distance[s] = 0
    distance_sleep[s] = 0
    distance_not_sleep[s] = 0
    time = 0
    Q = PriorityQueue()
    Q.put((0, s, time))

    while not Q.empty():

        (cur_distance, v,time) = Q.get()
        if cur_distance > distance[v] and cur_distance > distance_sleep[v]: continue

        for v_son, weight in G[v]:
            dist = cur_distance + weight
            if dist+8 < distance_sleep[v_son] and time+weight<=16: #spanie w v_son
                distance_sleep[v_son]= dist+8
                Q.put((dist + 8, v_son,0))
            
            if distance_not_sleep[v_son] > time + weight and dist < distance_sleep[v_son] and time+weight<=16: #spanie nie optymalnie ale w v_son mamy mniej nie przespanych godzin
                distance_not_sleep[v_son]=time+weight
                Q.put((dist, v_son,time + weight))

            if dist < distance[v_son] and time+weight<=16: #nie spanie w v_son
                distance[v_son] = dist
                distance_not_sleep[v_son]=time + weight
                Q.put((dist, v_son,time + weight))

    return min(distance[e],distance_sleep[e])


def warrior( G, s, t):
  n=0
  for u,v,w in G:
    n=max(n,u,v)
  G_son=[[] for _ in range(n+1)]
  for u,v,weight in G:
      G_son[u].append((v,weight))
      G_son[v].append((u,weight))

      
  return dijkstra(G_son,s,t)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( warrior, all_tests = True )
