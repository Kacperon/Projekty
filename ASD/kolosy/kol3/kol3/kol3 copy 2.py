#Kacper Feliks
from kol3testy import runtests


def orchard(T, m):
    słownik={}
    n=len(T)
    def reku(i=-1,j=0,k=0):
        if i==n-1:
            return k if j%m==0 else float("inf")
        for x in range(i+1):
            if (x,j,k) in słownik: return słownik[(x,j,k)]
        


        słownik[(i+1,j+T[i],k)]=reku(i+1,j+T[i],k)
        słownik[(i+1,j,k+1)]=reku(i+1,j,k+1)
        #return min(słownik[(i+1,j+T[i],k)],słownik[(i+1,j+T[i],k)])
    reku()
    wynik=float("inf")
    for i,j,k in słownik:
        if i==n-1 and j%m==0:
            wynik=min(wynik,k)

    return wynik


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(orchard, all_tests=True)
