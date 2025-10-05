import sys
import heapq

input = sys.stdin.readline
INF = 10**9

def dijkstra(start, graph, V):
    dist = [INF] * (V + 1)
    dist[start] = 0
    
    q = [(0, start)]
    
    while q:
        d, u = heapq.heappop(q)
        
        if d > dist[u]:
            continue
        
        for v, w in graph[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(q, (nd, v))
    return dist

V, E = map(int, input().split())
K = int(input())

graph = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    
    
dist = dijkstra(K, graph, V)

    
for i in range(1, V + 1):
    if dist[i] == INF:
        print("INF")
    else:
        print(dist[i])