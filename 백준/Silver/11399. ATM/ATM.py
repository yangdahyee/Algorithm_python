import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int, input().split()))

P.sort() 

timecheck = 0   
ans = 0   

for p in P:
    timecheck += p
    ans += timecheck

print(ans)