import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
targets = list(map(int, input().split()))

dq = deque(range(1, N + 1))
cnt = 0

for t in targets:
    idx = dq.index(t)
    left = idx
    right = len(dq) - idx
    
    if left <= right:
        dq.rotate(-left)
        cnt += left
        
    else:
        dq.rotate(right)
        cnt += right
        
    dq.popleft()
    
print(cnt)