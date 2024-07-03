# Kacper Feliks
from zad7testy import runtests


def maze(L):
    n = len(L)
    max_down = [[0]*(n) for _ in range(n+2)]
    max_up = [[0]*(n) for _ in range(n+2)]
    max_up[0][0] = 0
    max_down[0][0] = 0
    for i in range(n):
        for j in range(n):
            if L[i][j] == "#":
                max_down[i][j] = -float("inf")
                max_up[i][j] = -float("inf")
                
    for i in range(1, n):
        max_up[i][0] += max_up[i-1][0]+1
        max_down[i][0] += max_down[i-1][0]+1
        max_down[0][i] += max_down[0][i-1]+1
        max_up[0][i] += max_up[0][i-1]+1

    for i in range(1, n):

        if L[0][i] == ".":
            max_up[0][i] = max(max_up[0][i-1], max_down[0][i-1])+1

        for j in range(1, n):
            if L[j][i] == ".":
                max_up[j][i] = max(max_up[j-1][i], max_up[j]
                                   [i-1], max_down[j][i-1])+1

        if L[n-1][i] == ".":
            max_down[n-1][i] = max(max_up[n-1][i-1], max_down[n-1][i-1])+1

        for j in range(n-2, -1, -1):
            if L[j][i] == ".":
                max_down[j][i] = max(
                    max_down[j+1][i], max_up[j][i-1], max_down[j][i-1])+1

    return max_up[n-1][n-1] if max_up[n-1][n-1] != -float("inf") else -1


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(maze, all_tests=True)
