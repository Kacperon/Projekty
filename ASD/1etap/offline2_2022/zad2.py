#O(NlogN)
from zad2testy import runtests
def find(T, a):
    n = len(T)
    left = 0
    right = n - 1
    if a<T[0]:
        return 0
    while left <= right:
        mid = left + (right - left) // 2
        if T[mid] == a:
            while mid>0 and T[mid]==T[mid-1]:
                mid-=1
            return mid
        elif T[mid] < a:
            left = mid + 1
        else:
            right = mid - 1
    if T[mid]>a:
        mid-=1
    while mid>0 and T[mid]==T[mid-1]:
            mid-=1
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
        hoare_quicksort(T, p, pivot_index) # w jednym z wywołań nie omijamy pivota, bo jest on już na swoim miejscu
        hoare_quicksort(T, pivot_index + 1, r)
def sort_hoare(T):
     hoare_quicksort(T,0,len(T)-1)

def depth(L):
    n=len(L)
    T1,T2=[arr[0] for arr in L],[arr[1] for arr in L]
    sort_hoare(T1)
    sort_hoare(T2)
    max=0
    for i in range(n):
        fin=find(T2,L[i][1])#szukanie po końcu
        while fin<n-1 and T2[fin]==T2[fin+1]:#sukanie ostatniego który się nie powtarza 
            fin+=1
        curent=fin-find(T1,L[i][0])#liczba elementów w przedziale
        if max<curent:
            max=curent
            j=i
    return max

# T=[[1, 6], [1, 5], [1, 5], [8, 9], [1, 6]]
# print(depth(T))
runtests( depth ) 

