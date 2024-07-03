#Kacper Feliks
from kol3testy import runtests


def orchard(T, m):

    n=len(T)
    def reku(i=-1,j=0,k=0):
        if i==n-1:
            return k if j%m==0 else float("inf")
        return min(reku(i+1,j+T[i],k),reku(i+1,j,k+1))
    
    return reku()


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(orchard, all_tests=True)
