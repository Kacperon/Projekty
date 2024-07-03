#Kacper Feliks

from kol1testy import runtests

def maxrank(T):
  n=len(T)
  wynik=0
  for i in range(n):
    maxi=0
    element=T[i]
    for j in range(i-1,-1,-1):
      if element>T[j]:
        maxi+=1
    wynik=max(maxi,wynik)

  # tu prosze wpisac wlasna implementacje
  return wynik

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maxrank, all_tests = False )
