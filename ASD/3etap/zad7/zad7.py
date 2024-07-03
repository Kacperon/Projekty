# Kacper Feliks
from zad7testy import runtests


def maze(L):
    n = len(L)
    max_down = [0]*n
    max_up = [0]*n
    max_prev = [0]*n
    max_up[0] = 0
    max_down[0] = 0
    n2 = -(n**2)-2

    for i in range(1, n):
        max_down[i] = n2
        if L[i][0] == ".":
            max_up[i] += max_up[i-1]+1
        else:
            max_up[i] = n2

    for i in range(1, n):
        for j in range(0, n):
            # max
            max_prev[j] = max_up[j] if max_up[j] > max_down[j] else max_down[j]

        if L[0][i] == ".":
            max_up[0] = max_prev[0]+1
        else:
            max_up[0] = n2

        for j in range(1, n):
            if L[j][i] == ".":
                max_up[j] = max_up[j-1]+1 if max_up[j -
                                                    1] > max_prev[j] else max_prev[j]+1
            else:
                max_up[j] = n2

        if L[n-1][i] == ".":
            max_down[n-1] = max_prev[n-1]+1
        else:
            max_down[n-1] = n2

        for j in range(n-2, -1, -1):
            if L[j][i] == ".":
                max_down[j] = max_down[j+1] + \
                    1 if max_down[j+1] > max_prev[j] else max_prev[j]+1
            else:
                max_down[j] = n2

    return max_up[n-1] if max_up[n-1] > 0 else -1


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(maze, all_tests=True)
