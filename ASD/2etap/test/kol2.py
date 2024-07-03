from kol2testy import runtests

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)
        
        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1

def beautree(G):
    n = len(G)
    edges = []
    
    for u in range(n):
        for v, w in G[u]:
            if u < v:  # Ensure each edge is added only once
                edges.append((w, u, v))
    
    edges.sort()  # Sort edges by weight
    
    uf = UnionFind(n)
    mst_edges = []
    mst_weight = 0
    
    for w, u, v in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst_edges.append((w, u, v))
            mst_weight += w
            if len(mst_edges) == n - 1:
                break
    
    if len(mst_edges) != n - 1:
        return None
    
    m = mst_edges[0][0]
    M = mst_edges[-1][0]
    
    for w, u, v in edges:
        if (w < m or w > M) and (u, v) not in mst_edges and (v, u) not in mst_edges:
            continue
        if w >= m and w <= M and (u, v) not in mst_edges and (v, u) not in mst_edges:
            return None
    
    return mst_weight




# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( beautree, all_tests = False )
