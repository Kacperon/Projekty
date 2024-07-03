from zad9testy import runtests

def DAG(M):
    m, n = len(M), len(M[0])
    visited = [[False for _ in range(n)] for _ in range(m)]
    sorted = []
    move = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def DFSVisit(M, x,y):
        visited[x][y] = True

        for dx, dy in move:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and M[nx][ny] > M[x][y]:
                    DFSVisit(M,nx,ny)
        
        sorted.append((x,y))

    for x in range(m):
        for y in range(n):
            if not visited[x][y]:
                DFSVisit(M,x,y)


    return sorted[::-1]

def trip(M):
    m, n = len(M), len(M[0])
    dp = [[1 for _ in range(n)] for _ in range(m)]
    move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    max_path = 0

    sorted=DAG(M)

    for x,y in sorted:
        for dx, dy in move:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and M[nx][ny] > M[x][y]:
                dp[nx][ny]=dp[x][y]+1 if dp[x][y]+1>dp[nx][ny] else dp[nx][ny]
                max_path=max_path if max_path>=dp[nx][ny] else dp[nx][ny]
         
    return max_path


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(trip, all_tests=True)
