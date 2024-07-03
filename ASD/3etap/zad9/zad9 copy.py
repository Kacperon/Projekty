from zad9testy import runtests

from collections import deque


def trip(M):
    if not M or not M[0]:
        return 0

    m, n = len(M), len(M[0])
    
    # Directions for movement (right, left, up, down)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    # Initialize in-degrees and graph representation
    in_degree = [[0] * n for _ in range(m)]
    graph = [[[] for _ in range(n)] for _ in range(m)]

    # Build the graph and in-degree array
    for i in range(m):
        for j in range(n):
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and M[ni][nj] > M[i][j]:
                    graph[i][j].append((ni, nj))
                    in_degree[ni][nj] += 1

    # Initialize the queue with nodes having zero in-degree
    queue = deque([(i, j) for i in range(m) for j in range(n) if in_degree[i][j] == 0])
    
    # Distance array to store the longest path from each cell
    distance = [[1] * n for _ in range(m)]
    
    # Process nodes in topologically sorted order
    while queue:
        x, y = queue.popleft()
        
        for nx, ny in graph[x][y]:
            distance[nx][ny] = max(distance[nx][ny], distance[x][y] + 1)
            in_degree[nx][ny] -= 1
            if in_degree[nx][ny] == 0:
                queue.append((nx, ny))

    # Find the maximum distance from the distance array
    max_path = max(max(row) for row in distance)
    return max_path


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( trip, all_tests = True )
