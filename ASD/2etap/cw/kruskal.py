def list_edges(G):

    edges = []

    for v, row in enumerate(G):
        for u in row:
            if u[0] > v: edges.append((u[1],v,u[0]))

    edges.sort()
    return edges



def kruskal(G):

    def find(x):
        if parent[x] != x: parent[x] = find(parent[x])
        return parent[x]

    def union(x,y):
        x = find(x)
        y = find(y)

        if x==y:return
        if rank[x] > rank[y]: parent[y] = x
        else: 
            parent[x] = y
            if rank[x] == rank[y]: rank[y]+=1


    n = len(G)
    edges = list_edges(G)
    print(edges)
    parent = [i for i in range(n)]
    rank = [0 for _ in range(n)]

    mst = []
    for (w, u, v) in edges:
        if find(u) != find(v):
            union(u, v)
            mst.append((w,u,v))

    return mst


