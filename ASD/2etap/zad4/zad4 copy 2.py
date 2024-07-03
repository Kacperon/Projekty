#Kacper Feliks
#Mój program sortuje krawędzie grafu po wysokości
#następnie tworzy listę sąsiedstwa wszystkich krawędzi które mozna przelecieć na jednym minimalnym pułapie
#następnie algorytm BFS sprawdza na tej liście czy da sie przelecieć z x do y
#jak nie to listę sąsiedstwa aktualizujemy do następniej wysokości 
#i tak robimy aż sprawdzimy wszystkie opcje
#sortowanie ma złożoność O(ElogE) BFS O(E+V) a  oprację BFS wykonujemy E razy więc złożoność końcowa to
#O(E^2+E*V)
from zad4testy import runtests
from collections import deque

def BFS(G, x, y):
    n = len(G) # len(V)
    Q = deque()
    visited = [False for v in range(n)]
    visited[x] = True
    Q.append(x)
    while len(Q) > 0 and not visited[y]:
        u = Q.popleft()
        for v in G[u]: # dla każdego sąsiada u
            if not visited[v]:
                visited[v] = True
                Q.append(v)
    return visited[y]


def Flight(L,x,y,t):

  E=len(L)
  n=max(u[1] for u in L)
  n=max(n,y,x)
  G=[[]for _ in range(n+1)]
  L=sorted(L, key=lambda x: x[2])
  i,j=0,0

  while j<E and L[j][2]-L[i][2]<=2*t:
    G[L[j][0]].append(L[j][1])
    G[L[j][1]].append(L[j][0])
    j+=1
  flag=False
  bfs_flag=True

  while not flag and j<E+1 and i<E:

    if bfs_flag and G[y]!=[] and G[x]!=[]:
      flag=BFS(G,x,y)
      bfs_flag=False
      #end if
    G[L[i][0]].remove(L[i][1])
    G[L[i][1]].remove(L[i][0])
    i+=1
    while j<E and L[j][2]-L[i][2]<=2*t:
      G[L[j][0]].append(L[j][1])
      G[L[j][1]].append(L[j][0])
      j+=1
      bfs_flag=True

  return flag

# # zmien all_tests na True zeby uruchomic wszystkie testy
runtests( Flight, all_tests = True )


T=[(0,2,10),(0,3,10),(0,4,500)]
print(Flight(T,0,4,10))