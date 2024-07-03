# O(V^3)
def floyd_warshall(G):
    n=len(G)
    dist = [[float('inf')] * n for _ in range(n)]
    
    for i in range(n):
        for j, weight in G[i]:
            dist[i][j] = weight
    
    for i in range(n):
        dist[i][i] = 0
    
    # Algorytm Floyda-Warshalla
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    return dist