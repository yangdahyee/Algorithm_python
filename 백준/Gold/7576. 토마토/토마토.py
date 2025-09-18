import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

q = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


for r in range(N):
    for c in range(M):
        if matrix[r][c] == 1:
            q.append((r, c))
            
            
while q:
    x, y = q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and matrix[nx][ny] == 0:
            matrix[nx][ny] = matrix[x][y] + 1
            q.append((nx, ny))
            
ans = 0
for row in matrix:
    for el in row:
        if el == 0:
            print(-1)
            sys.exit(0)
    ans = max(ans, max(row))

print(ans - 1)