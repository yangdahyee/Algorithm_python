import sys
from collections import deque
input = sys.stdin.readline


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if grid[nx][ny] == grid[x][y]:
                    visited[nx][ny] = 1
                    q.append((nx, ny))


N = int(input().strip())
grid = [list(input().strip()) for _ in range(N)]

# 일반
visited = [[0] * N for _ in range(N)]
normal = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            BFS(i, j)
            normal += 1


# 적록색약
for i in range(N):
    for j in range(N):
        if grid[i][j] == 'G':
            grid[i][j] = 'R'

visited = [[0] * N for _ in range(N)]
redgreen = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            BFS(i, j)
            redgreen += 1

print(normal, redgreen) 