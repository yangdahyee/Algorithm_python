import sys
input = sys.stdin.readline

M, N = map(int,input().split())
lst = []

for num in range(M, N + 1): 
    if num == 1:
        continue
    for j in range(2, int(num**0.5) + 1):
        if num % j == 0:
            break
    else:
        print(num)