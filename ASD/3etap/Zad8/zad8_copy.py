# Kacper Feliks
#O(n*m)
from zad8testy import runtests

def parking(X, Y):
    m = len(Y)
    n = len(X)
    inf = (abs(X[0]-Y[m-1]))*n
    f = [[inf]*(m) for _ in range(n)]
    for j in range(m):
        f[0][j] = abs(X[0]-Y[j])
    for i in range(1, n):
        min_sum = inf
        for j in range(i, m):
            min_sum = min_sum if min_sum <= f[i-1][j-1] else f[i-1][j-1]#min
            f[i][j] = min_sum + abs(X[i]-Y[j])
    min_sum = inf

    for j in range(n-1, m):#min
        min_sum = min_sum if min_sum <= f[n-1][j] else f[n-1][j]

    return min_sum


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(parking, all_tests=True)
