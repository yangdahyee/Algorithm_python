import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, input().split())
    board[B].append(A)

best = 0
ans = []

for start in range(1, N + 1):
    visited = [False] * (N + 1)
    stack = [start]
    visited[start] = True
    cnt = 1

    while stack:
        cur = stack.pop()
        for nxt in board[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                stack.append(nxt)
                cnt += 1

    if cnt > best:
        best = cnt
        ans = [start]
    elif cnt == best:
        ans.append(start)

print(*ans)