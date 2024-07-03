import heapq

def prim(adjacency_list):
    n = len(adjacency_list)
    visited = [False] * n
    min_heap = [(0, 0)]  # (waga, wierzchołek startowy)
    mst_cost = 0
    mst_edges = []

    while min_heap:
        weight, u = heapq.heappop(min_heap)
        if visited[u]:
            continue
        visited[u] = True
        mst_cost += weight
        
        for v, w in adjacency_list[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (w, v))
                mst_edges.append((u, v, w))
    
    return mst_cost, mst_edges