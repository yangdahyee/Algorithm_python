from collections import deque

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    queue = deque()
    for i in range(N):
        queue.append((arr[i], i))

    cnt = 0

    while queue:
        cur = queue.popleft()

        for q in queue:
            if cur[0] < q[0]:
                queue.append(cur) 
                break
        else:
            cnt += 1
            if cur[1] == M: 
                print(cnt)
                break