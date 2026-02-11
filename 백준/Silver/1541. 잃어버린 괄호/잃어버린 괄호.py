import sys
input = sys.stdin.readline

parts = input().strip().split('-')
nums = []

for part in parts:
    total = 0
    tmp = part.split('+')
    for x in tmp:
        total += int(x)
    nums.append(total)

ans = nums[0]
for i in range(1, len(nums)):
    ans -= nums[i]

print(ans)
