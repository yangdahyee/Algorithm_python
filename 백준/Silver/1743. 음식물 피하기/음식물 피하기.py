import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())

grid = [[0] * (M + 1) for _ in range(N + 1)]
visited = [[False] * (M + 1) for _ in range(N + 1)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for _ in range(K):
    r, c = map(int, input().split())
    grid[r][c] = 1

ans = 0

for i in range(1, N + 1):
    for j in range(1, M + 1):
        if grid[i][j] == 1 and not visited[i][j]:
            stack = [(i, j)]
            visited[i][j] = True
            cnt = 1

            while stack:
                r, c = stack.pop()
                for k in range(4):
                    nr, nc = r + dx[k], c + dy[k]

                    if 1 <= nr <= N and 1 <= nc <= M and not visited[nr][nc]:
                        if grid[nr][nc] == 1:
                            visited[nr][nc] = True
                            stack.append((nr, nc))
                            cnt += 1

            ans = max(ans, cnt)



print(ans)
