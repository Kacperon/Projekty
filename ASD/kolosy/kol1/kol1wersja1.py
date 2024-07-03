#Kacper Feliks
#Mój program na początku kopjuje tablicę następnie sortuje kopię tablicy hoare_quicksortem
#
from kol1testy import runtests
def find(T, a):# szukanie binarne w posortowanej tablicy złożoność O(logN+k) gdzie k to liczba takich samych elementów
  n = len(T)
  left = 0
  right = n - 1
  if a < T[0]:
    return 0
  while left <= right:
    mid = left + (right - left) // 2
    if T[mid] == a:
      while mid > 0 and T[mid] == T[mid-1]:
        mid -= 1
      return mid
    elif T[mid] < a:
      left = mid + 1
    else:
      right = mid - 1
  while mid>0 and T[mid] == T[mid-1]:
        mid -= 1
  return mid
def hoare_partition(T, p, r):
   x = T[(p + r) // 2]
   i = p - 1
   j = r + 1
   while True:
     j -= 1
     while not T[j] <= x:
       j -= 1
     i += 1
     while not T[i] >= x:
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
  T_sorted = T[:]
  sort_hoare_quick(T_sorted)
  for i in range(n-1,-1,-1):
    ranga = find(T_sorted,T[i]) - n+i+1
    wynik = max(wynik,ranga)
  # tu prosze wpisac wlasna implementacje
  return wynik

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maxrank, all_tests = True )