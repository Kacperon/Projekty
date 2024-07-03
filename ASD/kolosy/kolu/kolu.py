from kolutesty import runtests
def DAG(G):
    n = len(G)
    visited = [None] * n
    sorted = [None] * n
    k = n - 1

    def DFSVisit(G, u):
        nonlocal k
        visited[u] = True

        for v in G[u]:
            if not visited[v]:
                DFSVisit(G, v)

        sorted[k] = u
        k -= 1

    for u in range(n):
        if not visited[u]:
            DFSVisit(G, u)

    return sorted

def projects(n, L):

  G=[[]for _ in range(n)]

  for i in L:
    G[i[0]].append(i[1])
  sorted=DAG(G)
  d=[1 for _ in range(n)]

  for i in sorted:
      for j in G[i]:
          d[j]=max(d[i]+1,d[j])
      
    
  return max(d)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( projects, all_tests = True )
