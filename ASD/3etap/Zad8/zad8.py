# Kacper Feliks
# O(n*m)
from zad8testy import runtests

def parking(X, Y):
    m = len(Y)
    n = len(X)
    f = [0]*(m)
    inf = float("inf")
    for j in range(m):
        f[j] = abs(X[0]-Y[j])
    for i in range(1, n):
        min_sum = inf
        zap = 0
        for j in range(i, m):
            min_sum = min_sum if min_sum <= f[j-1] else f[j-1]  # min
            f[j-1] = zap
            zap = min_sum + abs(X[i]-Y[j])
        f[j] = zap
    min_sum = inf

    for j in range(n-1, m):  # min
        min_sum = min_sum if min_sum <= f[j] else f[j]

    return min_sum


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(parking, all_tests=True)