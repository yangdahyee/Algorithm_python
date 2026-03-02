import sys
input = sys.stdin.readline

N = int(input())

s = 0
cube_sum = 0

for i in range(1, N + 1):
    s += i
    cube_sum += i ** 3

print(s)
print(s ** 2)
print(cube_sum)