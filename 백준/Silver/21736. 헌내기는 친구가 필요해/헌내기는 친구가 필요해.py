import sys
input = sys.stdin.readline

N, M = map(int, input().split())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

campus = []
sx, sy = -1, -1

for i in range(N):
    row = list(input().strip())
    campus.append(row)

    if sx == -1:
        for j in range(M):
            if row[j] == 'I':
                sx, sy = i, j
                break

visited = [[False] * M for _ in range(N)]
stack = [(sx, sy)]
visited[sx][sy] = True
cnt = 0

while stack:
    x, y = stack.pop()
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and campus[nx][ny] != 'X':
            visited[nx][ny] = True
            if campus[nx][ny] == 'P':
                cnt += 1
            stack.append((nx, ny))

print(cnt if cnt > 0 else "TT")
