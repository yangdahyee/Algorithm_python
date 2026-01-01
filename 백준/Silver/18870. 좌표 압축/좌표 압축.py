import sys
input = sys.stdin.readline

N = int(input())
X = list(map(int,input().split()))

temp = sorted(set(X))

ans = {}

for i, v in enumerate(temp):
    ans[v] = i

for x in X:
    print(ans[x], end=' ')