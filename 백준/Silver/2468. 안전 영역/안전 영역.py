import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

max_h = 0
for i in range(N):
    for j in range(N):
        if board[i][j] >= max_h:
            max_h = board[i][j]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

ans = 0
for h in range(0, max_h):
    visited = [[False] * N for _ in range(N)]
    cnt = 0

    for i in range(N):
        for j in range(N):
            if board[i][j] > h and not visited[i][j]:
                cnt += 1
                visited[i][j] = True
                q = deque()
                q.append((i, j))

                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < N and 0 <= ny < N:
                            if board[nx][ny] > h and not visited[nx][ny]:
                                visited[nx][ny] = True
                                q.append((nx, ny))

    if cnt > ans:
        ans = cnt

print(ans)