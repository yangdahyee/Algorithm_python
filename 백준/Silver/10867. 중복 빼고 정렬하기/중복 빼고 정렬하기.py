import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

nums = set(nums)
nums = sorted(nums)
print(*nums)