from egz1btesty import runtests


def planets(D, C, T, E):
    E += 1
    n = len(D)
    inf = float("inf")
    F = [[inf]*E for _ in range(n)]
    for b in range(E):
        F[0][b] = b*C[0]

    F[T[0][0]][0] = T[0][1]

    for i in range(1, n):
        for b in range(E):
            if b+D[i]-D[i-1] < E:
                F[i][b] = min(F[i][b], F[i-1][b+D[i]-D[i-1]])
            if b > 0:
                F[i][b] = min(F[i][b], F[i][b-1]+C[i])

        F[T[i][0]][0] = min(F[i][0]+T[i][1], F[T[i][0]][0])

    return F[n-1][0]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(planets, all_tests=True)
