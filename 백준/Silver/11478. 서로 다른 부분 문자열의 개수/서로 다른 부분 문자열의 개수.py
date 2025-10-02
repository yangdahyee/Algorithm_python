import sys
input = sys.stdin.readline

S = input().strip()
N = len(S)

ans = set()

for i in range(N):
    for j in range(i, N):
        ans.add(S[i:j+1])
        
print(len(ans))