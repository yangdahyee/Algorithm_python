nums = list(map(int, input().split()))
total = 0
for num in nums:
    total += num ** 2
ans = total % 10
print(ans)
