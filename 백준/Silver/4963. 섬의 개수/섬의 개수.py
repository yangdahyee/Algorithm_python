import sys
input = sys.stdin.readline

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1,  0,  1,-1, 1,-1, 0, 1]

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    grid = [list(map(int, input().split())) for _ in range(h)]
    islands = 0

    for i in range(h):
        for j in range(w):
            if grid[i][j] == 1:
                islands += 1
                grid[i][j] = 0

                stack = [(i, j)]
                while stack:
                    x, y = stack.pop()
                    for k in range(8):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < h and 0 <= ny < w and grid[nx][ny] == 1:
                            grid[nx][ny] = 0
                            stack.append((nx, ny))

    print(islands)