import sys
from collections import deque

input = sys.stdin.readline

N, L = map(int, input().split())
A = list(map(int, input().split()))
dq = deque()

for i in range(N):
    while dq and dq [-1][0] > A[i]:
        dq.pop()
    dq.append((A[i], i))

    if dq[0][1] <= i - L :
        dq.popleft()
    print(dq[0][0], end=' ')