import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
cnt = 0

for num in nums:
    if num == 1:
        continue

    for j in range(2, num):
        if num % j == 0: 
            break
    else:
        cnt += 1

print(cnt)