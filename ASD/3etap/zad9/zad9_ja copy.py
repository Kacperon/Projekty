from zad9testy import runtests
from collections import deque
import heapq as h

def trip(M):
    m, n = len(M), len(M[0])
    dp = [[-1 for _ in range(n)] for _ in range(m)]
    move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    max_path = 0
    Q = []
    for x in range(m):
        for y in range(n):
            flag = True
            for dx, dy in move:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not M[nx][ny] > M[x][y]:
                    flag = False
            if flag:
                h.heappush(Q,(M[x][y],x,y))
                dp[x][y] = 1

    while len(Q) > 0:

        height,x, y = h.heappop(Q)
        dist=dp[x][y]
        for dx, dy in move:
            nx, ny = dx+x, dy+y
            if 0 <= nx < m and 0 <= ny < n and M[nx][ny] > M[x][y] and dp[nx][ny]==-1:
                dist= max(dist, dp[nx][ny]+1)
                Q.append((M[nx][ny],nx,ny))
            dp[x][y]=dist
    max_path=max(max(dp[i]) for i in range(m))
    return max_path


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(trip, all_tests=True)