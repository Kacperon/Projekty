"""
  Kacper Kopiec
  Złożoność czasowa: O(n logn)
  Zlożoność pamięciowa: O(n)

  Algorytm rozpoczyna się "skalowaniem" danych, to znaczy zmniejszenie wartości elementów tablicy T
  z zachowaniem relacji nierówności pomiędzy nimi (np. [5, 3, 9, 4] -> [2, 0, 3, 1]).
  Dzięki skalowaniu maksymalny element będzie zawsze < n, gdzie n = len(T)
  Skalowanie wykonujemy poprzez zbudowanie posortowanej tablicy bez duplikatów zawietającej każdy element z tablicy T
  Następnie nową wartością elementu i-tego będzie indeks T[i] w nowej tablicy.
  Skalowanie zajmie:
    czasowo: O(n logn) - dla każdej liczby wykonujemy binary searcha + sortowanie merge_sortem
    pamięciowo: O(n) - nowa tablica będzie miała maksymalnie n elementów 

  Następnie korzystając ze stryktury danych zwanej drzewem przedziałowym, które wspiera takie operacje jak:
      1) Dodawanie krotności elemntu do drzewa, to znaczy można dodać że element 2 wystąpił już 3 razy - add(x, k)
      2) Suma elementów w przedziale [a, b], gdzie a i b to liczby naturalne - query(a, b)
    Dzięki skalowaniu złożoność pamięciowa tego drzewa będzie wynosiła O(n)
    Wysokość będzie wynosiła log n, więc obie operacje będą wykonywały się w złożoności O(log n)
  będziemy przechodzili po tablicy T:
    ranga i-tego elementu będzie wynosiła query(0, T[i] - 1)
    skoro element się pojawił to dodajemy jego wystąpienie add(T[i], 1)
  Obie operacje wykonują się w O(log n) i robimy to dla każdego elementu, końcowo: O(n logn)

  Algorytm działa, ponieważ do rangi elementu liczą się tylko elementy z mniejszym indeksem, a je już dodaliśmy,
  więc wystaczy sprawdzić ile mniejszych.
"""
from kol1testy import runtests

class SegmentTree:
  # Pamięć O(n)
  def __init__(self, n):
    p = 1
    while not ((1 << p) - (1 << (p - 1)) >= n): p += 1 # liczba liści musi być większa lub równa ilośći elementów
    self.M = (1 << (p - 1)) # indeks pierwszego liścia
    self.tree = [0] * (1 << p)
  
  # Dodawanie elementu O(logn)
  def add(self, a, v):
    a += self.M
    self.tree[a] += v
    a //= 2
    while a:
      self.tree[a] = self.tree[2 * a] + self.tree[2 * a + 1]
      a //= 2
  
  # Suma elementów z przedziału [a, b] O(logn)
  def query(self, a, b):
    if b < a: return 0
    a += self.M
    b += self.M
    ans = self.tree[a]
    if a != b: ans += self.tree[b]
    while a // 2 != b // 2:
      if a % 2 == 0: ans += self.tree[a + 1]
      if b % 2 == 1: ans += self.tree[b - 1]
      a //= 2
      b //= 2
    return ans

def merge_sort(T):
  if len(T) <= 1: return T

  L, R, a, b, idx = merge_sort(T[0:len(T) // 2]), merge_sort(T[len(T) // 2:]), 0, 0, 0
  while a < len(L) and b < len(R):
    if L[a] <= R[b]:
      T[idx] = L[a]
      a += 1
    else:
      T[idx] = R[b]
      b += 1
    idx += 1
  
  while a < len(L):
    T[idx] = L[a]
    a += 1
    idx += 1
  
  while b < len(R):
    T[idx] = R[b]
    b += 1
    idx += 1
  
  return T

# binary search - O(log n)
def bs(T, x):
  l, r = 0, len(T) - 1
  while l <= r:
    mid = (l + r) // 2
    if T[mid] == x: return mid
    if T[mid] > x: r = mid - 1
    else: l = mid + 1
  return -1

def maxrank(T):
  if len(T) == 0: return 0

  # Skalowanie danych
  tmp = T[:]
  tmp = merge_sort(tmp)
  uniq = [tmp[0]]
  for x in tmp:
    if x != uniq[-1]:
      uniq.append(x)
  
  for i in range(len(T)):
    T[i] = bs(uniq, T[i])
  
  # Główna część algorytmu
  ST = SegmentTree(len(uniq))
  ans = 0
  for x in T:
    ans = max(ans, ST.query(0, x - 1))
    ST.add(x, 1)
  
  return ans

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maxrank, all_tests = True )
