from zad9testy import runtests
from queue import Queue

def trip(M):
    m, n = len(M), len(M[0])
    dp = [[-1 for _ in range(n)] for _ in range(m)]
    
    def dfs(x, y):
        stack = [(x, y)]
        path_stack = []

        while stack:
            cx, cy = stack.pop()
            if dp[cx][cy] == -1:
                path_stack.append((cx, cy))
                dp[cx][cy] = 0  # Oznaczamy węzeł jako odwiedzony, ale jeszcze nie przetworzony
                stack.append((cx, cy))  # Dodajemy z powrotem na stos, aby przetworzyć po sąsiadach
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = cx + dx, cy + dy
                    if 0 <= nx < m and 0 <= ny < n and M[nx][ny] > M[cx][cy]:
                        if dp[nx][ny] == -1:
                            stack.append((nx, ny))
            else:
                if dp[cx][cy] == 0:
                    longest_path = 1  # Ścieżka minimalna zawiera tylko bieżący węzeł
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nx, ny = cx + dx, cy + dy
                        if 0 <= nx < m and 0 <= ny < n and M[nx][ny] > M[cx][cy]:
                            longest_path = max(longest_path, 1 + dp[nx][ny])
                    dp[cx][cy] = longest_path

        return dp[x][y]

    max_path = 0
    for i in range(m):
        for j in range(n):
            max_path = max(max_path, dfs(i, j))

    return max_path


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( trip, all_tests = True )
