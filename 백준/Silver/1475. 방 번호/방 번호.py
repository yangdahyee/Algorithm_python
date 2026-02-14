import sys
input = sys.stdin.readline

nums = input().strip()
cnt = [0] * 10

for num in nums:
    cnt[int(num)] += 1

check = (cnt[6] + cnt[9] + 1) // 2
cnt[6] = check
cnt[9] = 0

print(max(cnt))