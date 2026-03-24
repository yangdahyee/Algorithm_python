import sys
input = sys.stdin.readline

n = int(input())
lst = [0] + list(map(int, input().split()))
s = int(input())
visited = [False] * (n + 1)

stack = [s]
visited[s] = True
cnt = 1

while stack:
    cur = stack.pop()
    d = lst[cur]

    for nxt in [cur + d, cur - d]:
        if 1 <= nxt <= n and not visited[nxt]:
            visited[nxt] = True
            stack.append(nxt)
            cnt += 1

print(cnt)