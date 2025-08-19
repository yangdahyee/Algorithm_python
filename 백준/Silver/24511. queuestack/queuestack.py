import sys
from collections import deque

input = sys.stdin.readline

N = int(input().strip())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = int(input().strip())
C = list(map(int, input().split()))

lst = []
for i in range(N):
    if A[i] == 0:
        lst.append(B[i])
        
queuestack = deque(reversed(lst))


if not queuestack:
    print(*C)
else:
    ans = []
    for el in C:
        ans.append(queuestack.popleft())  
        queuestack.append(el)             
    print(*ans)