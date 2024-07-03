from zad7testy import runtests


def maze(L):
    n = len(L)
    visited = [[False]*(n+1) for _ in range(n+1)]
    cunter = -1

    def reku(L, visited, i=0, j=0, cunt=0):
        nonlocal cunter
        visited[i][j] = True
        if i != n-1 or j != n-1:
            if i < n-1 and not visited[i+1][j] and L[i+1][j] != "#":
                reku(L, visited, i+1, j, cunt+1)
            if j < n-1 and not visited[i][j+1] and L[i][j+1] != "#":
                reku(L, visited, i, j+1, cunt+1)
            if i > 0 and not visited[i-1][j] and L[i-1][j] != "#":
                reku(L, visited, i-1, j, cunt+1)
        else:
            cunter = max(cunter, cunt)
        visited[i][j] = False

    reku(L, visited, 0, 0, 0)

    return cunter


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(maze, all_tests=True)
