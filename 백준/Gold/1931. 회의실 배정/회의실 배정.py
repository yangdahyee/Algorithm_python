import sys
input = sys.stdin.readline

N = int(input())
meetings = [list(map(int, input().split())) for _ in range(N)]

meetings.sort(key=lambda x: (x[1], x[0]))

cnt = 0
current_end = 0

for s, e in meetings:
    if s >= current_end:
        cnt += 1
        current_end = e

print(cnt)