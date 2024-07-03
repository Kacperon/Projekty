from egz1btesty import runtests


def kstrong( T, k):
  n=len(T)

  F=[[0 for _ in range(k+1)]for _ in range(n)]

  F[0][0]=max(T[0],0)
  for i in range(1,n):
    F[i][0]=max(F[i-1][0]+T[i],T[i])
  for i in range(1,n):
    for kj in range(1,k+1):
      F[i][kj]=max(F[i-1][kj-1],F[i-1][kj]+T[i])

  return F[n-1][k]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( kstrong, all_tests = True )
