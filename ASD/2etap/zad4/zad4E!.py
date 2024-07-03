from zad4testy import runtests

def Flight(L,x,y,t):
  n=max(u[1] for u in L)
  G=[[]for _ in range(n+1)]
  for u in L:
    G[u[0]].append([u[1],u[2],False])
    G[u[1]].append([u[0],u[2],False])
  flag=False
  def DFS(G,x,y,t,mini=float("inf"),maxi=0):
    nonlocal flag
    if maxi-mini>2*t or flag: return
    if x==y:
      flag=True
      return
    for u in G[x]:
      if not u[2]:
        u[2]=True
        for v in G[u[0]]:
          if v[0]==x:
            v[2]=True
        DFS(G,u[0],y,t,min(mini,u[1]),max(maxi,u[1]))
        u[2]=False
        for v in G[u[0]]:
          if v[0]==x:
            v[2]=False
  DFS(G,x,y,t)
  return flag

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( Flight, all_tests = True )

# T=[(i,j,0)for i in range(100) for j in range(100)]
# print(Flight(T,0,100,20))
# T=[(0,i,10)for i in range(1_000_000)]
# print(Flight(T,0,1_000_000,10))
