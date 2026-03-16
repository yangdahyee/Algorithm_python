import sys
input = sys.stdin.readline

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(M)]

dr = [1, 0]
dc = [0, 1]

visited = [[False] * N for _ in range(M)]
stack = [(0, 0)]
visited[0][0] = True

while stack:
    r,c = stack.pop()
    if r == M - 1 and c == N - 1:
        print("Yes")
        break
    for k in range(2):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < M and 0 <= nc < N:
            if grid[nr][nc] == 1 and not visited[nr][nc]:
                visited[nr][nc] = True
                stack.append((nr, nc))

else:
    print("No")
