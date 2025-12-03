import sys 
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    X, Y = map(int, input().split())
    arr.append((X, Y))

arr.sort()

for X, Y in arr:
    print(X, Y)