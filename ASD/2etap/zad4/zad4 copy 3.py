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
class Node():
   def __init__(self,val=None,next=None):
      self.val=val
      self.next=next

def BFS(G, x, y):
    n = len(G) # len(V)
    Q = deque()
    visited = [False for v in range(n)]
    visited[x] = True
    Q.append(x)
    while len(Q) > 0 and not visited[y]:
        u = Q.popleft()
        p=G[u][0]
        while p and p.next: # dla każdego sąsiada u
            p=p.next
            if not visited[p.val]:
                visited[p.val] = True
                Q.append(p.val)
    return visited[y]


def Flight(L, x, y, t):
  n = max(max(u[1] for u in L), x, y) + 1
  G = [[Node(),None] for _ in range(n)]
  for i in G: i[1]=i[0]

  L = sorted(L, key=lambda x: x[2])
  i, j, E = 0, 0, len(L)
  while j < E:
    while j < E and L[j][2] - L[i][2] <= 2*t:
      G[L[j][0]][1].next=Node(L[j][1])
      G[L[j][0]][1]=G[L[j][0]][1].next
      G[L[j][1]][1].next=Node(L[j][0])
      G[L[j][1]][1]=G[L[j][1]][1].next
      j += 1
    if G[x] != [] and G[y] != [] and BFS(G, x, y):
      return True
    while j < E and L[j][2] - L[i][2] > 2*t:
      G[L[i][0]][0]=G[L[i][0]][0].next
      G[L[i][1]][0]=G[L[i][1]][0].next
      i += 1
  return False

# # zmien all_tests na True zeby uDruchomic wszystkie testy
# runtests( Flight, all_tests = True )

T=[(0,i,10)for i in range(1_000_000)]
print(Flight(T,0,1_000_000,10))
