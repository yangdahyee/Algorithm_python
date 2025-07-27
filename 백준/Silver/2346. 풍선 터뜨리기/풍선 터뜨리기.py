from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
balloons = deque(enumerate(map(int, input().split())))

ans = []

while balloons:
    idx, num = balloons.popleft()
    ans.append(idx + 1)

    if not balloons:
        break

    if num > 0:
        balloons.rotate(-(num - 1))
    else:
        balloons.rotate(-num)

print(*ans)