import sys
input = sys.stdin.readline

N = int(input())
arr = []

for _ in range(N):
    X, Y = map(int, input().split())
    arr.append((Y, X))
    
arr.sort()

for Y, X in arr:
    print(X, Y)
    