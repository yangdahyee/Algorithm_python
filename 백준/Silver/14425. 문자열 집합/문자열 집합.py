import sys
input = sys.stdin.readline

N, M = map(int,input().split())
S = set(input().strip() for _ in range(N))
cnt = 0
    
for _ in range(M):
    check = input().strip()
    if check in S:
        cnt += 1
        
print(cnt)