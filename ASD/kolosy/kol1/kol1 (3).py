#Jan Sarba
#Najpierw tworze z T tablice tablic T2, w ktorej zapisuje dla kazdego i: wartosc T[i],
#miejsce w pierwotnej tablicy T, i miejsce w tablicy T2 po posortowaniu (wstepnie wszedzie 0).
#Nastepnie sortuje T2 malejaco stabilnym mergesortem i uzupelniam, gdzie co wyladowalo.
#Element, ktory pokonal najwieksza droge do przodu po posortowaniu byl wiekszy od najwiekszej ilosci
#jego przodownikow w pierwotnej tabeli. Znajduje go i wyliczam dla niego rank.
#Zlozonosc szacuje na O(nlogn + n), wiec ostatecznie O(nlogn).
from kol1testy import runtests

def merge(A,B):
    n=len(A)
    m=len(B)
    a,b=0,0
    C=[0 for _ in range(n+m)]
    while a<n and b<m:
        if A[a][0]>B[b][0]:
            C[a+b]=A[a]
            a+=1
        else:
            C[a+b]=B[b]
            b+=1
    while a<n:
        C[a+b]=A[a]
        a+=1
    while b<m:
        C[a+b]=B[b]
        b+=1
    return C

def msort(T):
    n=len(T)
    if n<=1:
        return T
    m=n//2
    A=T[:m]
    B=T[m:]
    A=msort(A)
    B=msort(B)
    return merge(A,B)

def rank(T,i):
    sum=0
    for j in range(i-1,-1,-1):
        if T[j]<T[i]:
            sum+=1
    return sum

def maxrank(T):
    n=len(T)
    T2=[[T[i],i,0] for i in range(n)]
    T2=msort(T2)
    maxind=0
    maxdiff=0
    for i in range(n):
        T2[i][2]=i
        currdiff=T2[i][1]-T2[i][2]
        if currdiff>maxdiff:
            maxdiff=currdiff
            maxind=T2[i][1]
        
    return rank(T,maxind)

def maxrank1(T):
    maxi=0
    sum=0
    n=len(T)
    for i in range(n-1,-1,-1):
        sum=0
        for j in range(i-1,-1,-1):
            if T[i]>T[j]:
              sum+=1
        if sum>maxi:
            maxi=sum
    return maxi



# zmien all_tests na True zeby uruchomic wszystkie testy
# runtests( maxrank, all_tests = True )
t=[1,2,1,1]
print(maxrank(t))