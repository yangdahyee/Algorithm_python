from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

visited = [[False] * N for _ in range(N)]
q = deque([(0, 0)])
visited[0][0] = True

while q:
    r, c = q.popleft()

    if r == N - 1 and c == N - 1:
        print("HaruHaru")
        break

    jump = board[r][c]

    if jump == 0:
        continue

    nr, nc = r + jump, c
    if nr < N and not visited[nr][nc]:
        visited[nr][nc] = True
        q.append((nr, nc))

    nr, nc = r, c + jump
    if nc < N and not visited[nr][nc]:
        visited[nr][nc] = True
        q.append((nr, nc))

else:
    print("Hing")