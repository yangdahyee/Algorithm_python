import sys
input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
for _ in range(T):
    H, W = map(int, input().split())
    grid = [list(input().strip()) for _ in range(H)]
    visited = [[False] * W for _ in range(H)]

    cnt = 0

    for i in range(H):
        for j in range(W):
            if grid[i][j] == '#' and not visited[i][j]:
                cnt += 1
                stack = [(i, j)]
                visited[i][j] = True

                while stack:
                    r, c = stack.pop()

                    for k in range(4):
                        nr = r + dr[k]
                        nc = c + dc[k]

                        if 0 <= nr < H and 0 <= nc < W:
                            if grid[nr][nc] == '#' and not visited[nr][nc]:
                                visited[nr][nc] = True
                                stack.append((nr, nc))

    print(cnt)