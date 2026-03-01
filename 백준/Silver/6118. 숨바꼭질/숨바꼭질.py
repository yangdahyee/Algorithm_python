from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dist = [-1] * (N + 1)
q = deque([1])
dist[1] = 0

while q:
    cur = q.popleft()
    for nxt in graph[cur]:
        if dist[nxt] == -1:
            dist[nxt] = dist[cur] + 1
            q.append(nxt)

max_dist = max(dist[1:])

ans_num = -1
cnt = 0

for i in range(1, N + 1):
    if dist[i] == max_dist:
        if ans_num == -1:
            ans_num = i
        cnt += 1

print(ans_num, max_dist, cnt)