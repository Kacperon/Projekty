#Kacper Feliks
#program oddziela pierwsze p elementów do nowej tablicy pomocniczej
#następnie sortuje tablicę pomocniczą za pomocą merge_sorta
#odczytuje z tablicy element o indeksie p-k
#i binarnie przeszukuje tablicę w celu usunięcia elementu pierwszego a następnie wstawienia pierwszego elementu którego nie ma w tablicy pomocniczej
#a następnie powtarza tą operację do końca tablicy
#sortowanie tablicy pomocniczej jest wykonane tylko raz o złożoności O(p*logp)
#szukanie i zamiana elementu w tablicy pomocniczej ma złożoność O(logp)
#a szukanie wykonujemy n-p razy z racji ze n>>p to złożoność programu to O(n*logp)
from zad2testy import runtests
def merge(T1,T2):#funkcja scalająca
    j1,j2=0,0
    n1,n2=len(T1),len(T2)
    n=n1+n2
    T3=[0]*n
    i=0
    while j1<n1 and j2<n2:
        if T1[j1]>T2[j2]:
            T3[i]=T2[j2]
            j2+=1
            i+=1
        else:
            T3[i]=T1[j1]
            j1+=1
            i+=1
    for j in range(j1,n1):
        T3[i]=T1[j]
        i+=1
    for j in range(j2,n2):
        T3[i]=T2[j]
        i+=1
    return T3
def merge_sort(T):#sortowanie przez scalanie
    if len(T) <= 1:
        return T
    mid = len(T) // 2
    left = merge_sort(T[:mid])
    right = merge_sort(T[mid:])

    return merge(left, right)
def find(T, a):#szukanie binarne
    n = len(T)
    left = 0
    right = n - 1
    if a<T[0]:
        return 0
    while left <= right:
        mid = left + (right - left) // 2
        if T[mid] == a:
            return mid
        elif T[mid] < a:
            left = mid + 1
        else:
            right = mid - 1
    if T[mid]>a:
        mid-=1
    return mid
def ksum(T, k, p):
    n=len(T)
    tp=[0 for _ in range(p)]
    for i in range(p):
        tp[i]=T[i]
    tp=merge_sort(tp)
    sum=0
    sum+=tp[p-k]
    for i in range(n-p):
        mid=find(tp,T[i])
        del tp[mid]
        mid=find(tp,T[i+p])
        tp.insert(mid+1,T[i+p])
        sum+=tp[p-k]
    # tu prosze wpisac wlasna implementacje
    return sum



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ksum, all_tests=True )
