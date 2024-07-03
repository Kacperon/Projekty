#Kacper Feliks
#mój algorytm to typowy algorytm dynamiczny który wypełnia tablicę F[i][k]
#na początku rospatruje warunki brzegowe F[i][0] jako max z:
#wartości poprzedniej plus wartość aktualna
#z wartości aktualnej (zmieniamy granicę przedziału)
#i 0 nie bierzemy naszego elementu
#następnie obliczamy resztę F[i][k] jako max z:
#wartości poprzedniej(poprzedni przedział) plus aktualna wartość
#i poprzedniego maksymalnego przedziału z pominięciem tego
#
# złożoność czasowa O(nk)
# złożoność pamięciowa O(nk)
from egz1btesty import runtests


def kstrong( T, k):
  
  n=len(T)

  F=[[0 for _ in range(k+1)]for _ in range(n)]

  F[0][0]=T[0]
  for i in range(1,n):
    F[i][0]=max(F[i-1][0]+T[i],T[i])
  maxi=0
  for kj in range(1,k+1):
    for i in range(1,n):
      F[i][kj]=max(F[i-1][kj-1],F[i-1][kj]+T[i])
      maxi=max(F[i][kj],maxi)#makszymalna suma
  

    
  return maxi

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( kstrong, all_tests = True )
