#O(VE)
def bellman_ford(G, start):
    n=len(G)
    distance = [float('inf')] * n
    distance[start] = 0

    # Relaksacja wszystkich krawędzi |V| - 1 razy
    for _ in range(n - 1):
        for u, v, w in G:
            if distance[u] != float('inf') and distance[u] + w < distance[v]:
                distance[v] = distance[u] + w

    # Sprawdzenie cykli o ujemnej wadze
    for u, v, w in G:
        if distance[u] != float('inf') and distance[u] + w < distance[v]:
            return None

    return distance