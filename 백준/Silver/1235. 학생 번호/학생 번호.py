import sys
input = sys.stdin.readline

N = int(input())
nums = [input().strip() for _ in range(N)]
L = len(nums[0])

for k in range(1, L + 1):
    ans = set()
    for student in nums:
        ans.add(student[-k:])
    if len(ans) == N:
        print(k)
        break