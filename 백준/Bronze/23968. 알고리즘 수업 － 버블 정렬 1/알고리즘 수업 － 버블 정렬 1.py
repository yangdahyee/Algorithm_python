import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))

cnt = 0

for last in range(N - 1, 0, -1):
    for i in range(0, last):
        if A[i] > A[i+1]:
            x, y = A[i], A[i+1]
            A[i], A[i+1] = A[i+1], A[i]
            cnt += 1

            if cnt == K:
                print(y, x)
                sys.exit(0)

print(-1)