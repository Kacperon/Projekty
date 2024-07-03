import heapq
from collections import defaultdict
from egz1atesty import runtests
def dijkstra(graph, start):
    pq = [(0, start)]
    dist = {start: 0}
    while pq:
        current_cost, u = heapq.heappop(pq)
        if current_cost > dist.get(u, float('inf')):
            continue
        for v, weight in graph[u]:
            cost = current_cost + weight
            if cost < dist.get(v, float('inf')):
                dist[v] = cost
                heapq.heappush(pq, (cost, v))
    return dist
def reverse_graph(graph):
    rev_graph = defaultdict(list)
    for u in graph:
        for v, w in graph[u]:
            rev_graph[v].append((u, w))
    return rev_graph
def build_extended_graph(G, B):
    graph = defaultdict(list)
    for u, v, w in G:
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    bike_graph = defaultdict(list)
    for i, p, q in B:
        bike_graph[i].append((p, q))
    
    return graph, bike_graph
def armstrong(B, G, s, t):
    graph, bike_graph = build_extended_graph(G, B)
    
    # Najkrótsze czasy biegu od początku
    run_times_from_start = dijkstra(graph, s)
    
    # Najkrótsze czasy biegu od końca
    rev_graph = reverse_graph(graph)
    run_times_from_end = dijkstra(rev_graph, t)
    
    min_time = float('inf')
    
    # Sprawdzamy wszystkie rowery
    for i, p, q in B:
        # Czas na bieg do roweru
        time_to_bike = run_times_from_start.get(i, float('inf'))
        if time_to_bike == float('inf'):
            continue
        
        # Czas na przejazd rowerem
        time_riding = q
        
        # Czas na dotarcie do końca od miejsca oddania roweru
        time_to_end = run_times_from_end.get(p, float('inf'))
        if time_to_end == float('inf'):
            continue
        
        # Całkowity czas
        total_time = time_to_bike + time_riding + time_to_end
        
        # Aktualizujemy minimalny czas
        min_time = min(min_time, total_time)
    
    return min_time

 # Wynik powinien być minimalnym czasem potrzebnym na pokonanie trasy

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( armstrong, all_tests = True )
