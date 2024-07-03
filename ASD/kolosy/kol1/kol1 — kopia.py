#Kacper Feliks

from kol1testy import runtests

def maxrank(T):
  n=len(T)
  wynik=0
  maxelement=T[n-1]
  i=n-1
  while i>wynik:
    maxi=0
    element=T[i]
    if i>maxi and element>maxelement:
      maxelement=element
      for j in range(i-1,-1,-1):
        if element>T[j]:
          maxi+=1
    wynik=max(maxi,wynik)
    i-=1
  return wynik

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maxrank, all_tests = True )
