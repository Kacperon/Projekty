#Kacper Feliks
#Mój program na początku powiększa tablicę o początkowe indeksy elementów
#następnie sortuje tablicę po wartościach elementów hoare_quicksortem( O(nlogn) )
#następnie po posortowanej tablicy przechodzi od końca i szuka elementu
#krórego ranga wyrażona pozycją w posortowanej tablicy minus jej odległość od końca w orginalnej
#ponieważ element dominuje wszyskie elementy mniejsze od niej bez tych które są za nią
#wiec mój algorym ma złozoność O(nlogn+n) co sprowadza sie do O(nlogn)
from kol1testy import runtests
#hoare_quicksort po 1 elemencie (quicksort z hoare_partition)
def hoare_partition(T, p, r):#po 1 elemencie
   x = T[(p + r) // 2][0]
   i = p - 1
   j = r + 1
   while True:
     j -= 1
     while not T[j][0] <= x:
       j -= 1
     i += 1
     while not T[i][0] >= x:
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
def sort_hoare_quick(T):
   hoare_quicksort(T, 0, len(T) - 1)



def maxrank(T):
  n = len(T)
  wynik = 0
  T = [[T[i],i] for i in range(n)]
  # sort_hoare_quick(T)#sortowanie tablicy po pierwszym elemencie
  sort_hoare_quick(T)
  i = n - 1
  while i >wynik:
    indeks = T[i][1]
    pozycja = i
    while i > 0 and T[i][0] == T[i-1][0]:#szukanie elementu o tej samej wartości z największym indeksem
      i -= 1
      indeks = max(indeks, T[i][1])
    ranga = indeks - (n-1-i)
    wynik = max(wynik, ranga )
    i -= 1
  return wynik

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maxrank, all_tests = True )
