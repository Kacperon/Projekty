from zad4testy import runtests
def hoare_partition(T, p, r):
   x = T[(p + r) // 2][2]
   i = p - 1
   j = r + 1
   while True:
     j -= 1
     while not T[j][2] <= x:
       j -= 1
     i += 1
     while not T[i][2] >= x:
       i += 1
     if i < j:
       T[i], T[j] = T[j], T[i]
     else:
       return j

def hoare_quicksort(T, p, r):
   if p < r:
     pivot_index = hoare_partition(T, p, r)
     hoare_quicksort(T, p, pivot_index)
     hoare_quicksort(T, pivot_index + 1, r)

def sort_hoare(T):
   hoare_quicksort(T, 0, len(T) - 1)

def Flight(L,x,y,t):
  E=len(L)
  n=max(u[1] for u in L)
  G=[[]for _ in range(n+1)]
  sort_hoare(L)
  flag=False
  i,j=0,0
  while j<E-1 and L[j+1][2]-L[i][2]<=2*t:
    j+=1
  for u in L[:(j+1)]:
      G[u[0]].append(u[1])
      G[u[1]].append(u[0])
  dfs_flag=True
  while not flag and j<E and i<E:

    if dfs_flag and len(G[y])>0:

      visited = [False]*(n+1)
      def DFS(G,x,y):
        nonlocal flag
        if flag: return
        if x==y:
          flag=True
          return
        for v in G[x]:
          if not visited[v]:
            visited[v]=True
            DFS(G,v,y)
        #end def
      DFS(G,x,y)
      dfs_flag=False
      #end if
    edge=(L[i][0],L[i][1])
    G[edge[0]].remove(edge[1])
    G[edge[1]].remove(edge[0])
    i+=1
    while j<E-1 and (L[j+1][2]-L[i][2]<=2*t or i==j+1):
      j+=1
      G[L[j][0]].append(L[j][1])
      G[L[j][1]].append(L[j][0])
      dfs_flag=True

  return flag

# # zmien all_tests na True zeby uruchomic wszystkie testy
runtests( Flight, all_tests = True )

