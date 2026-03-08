import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

arr = []
for i in range(N):
    arr.append((A[i], i))

arr.sort()

P = [0] * N

for j in range(N):
    v, idx = arr[j]
    P[idx] = j

print(*P)