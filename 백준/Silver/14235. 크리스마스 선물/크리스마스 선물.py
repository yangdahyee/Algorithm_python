import sys
import heapq as hq

input = sys.stdin.readline

n = int(input())
gifts = []

for _ in range(n):
    a = list(map(int,input().split()))
    if a[0] == 0:
        if gifts:
            print(-hq.heappop(gifts))
        else:
            print(-1)
            
    else:
        for gift in a[1:]:
            hq.heappush(gifts, -gift)
