import sys
input = sys.stdin.readline

S = int(input())
ans = 0
max_num = 0

for num in range(1, S+1):
    ans += num
    max_num += 1
    if ans > S:
        max_num -= 1
        break
        
print(max_num)