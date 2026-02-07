import sys
input = sys.stdin.readline

N, M = map(int, input().split())
grid = [input().strip() for _ in range(M)]
visited = [[False] * N for _ in range(M)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

w_ans = 0
b_ans = 0

for i in range(M):
    for j in range(N):
        if visited[i][j]:
            continue
        color = grid[i][j]
        visited[i][j] = True
        stack = [(i, j)]
        cnt = 1

        while stack:
            r, c = stack.pop()
            for k in range(4):
                nr, nc = r + dx[k], c + dy[k]
                if 0 <= nr < M and 0 <= nc < N and not visited[nr][nc] and grid[nr][nc] == color:
                    visited[nr][nc] = True
                    stack.append((nr, nc))
                    cnt += 1

        ans = cnt * cnt
        if color == 'W':
            w_ans += ans
        else:
            b_ans += ans

print(w_ans, b_ans)