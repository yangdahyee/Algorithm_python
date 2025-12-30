import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
MAX = 10 ** 5

visited = [-1] * (MAX + 1)

def bfs():
    q = deque()
    q.append(N)
    visited[N] = 0  
    
    while q:
        cur = q.popleft()
        
        if cur == K:
            return visited[cur]
        
        for i in (cur + 1, cur - 1, cur * 2):
            if 0 <= i <= MAX and visited[i] == -1:
                visited[i] = visited[cur] + 1
                q.append(i)

print(bfs())