import sys
input = sys.stdin.readline

n = int(input())
stack = []
ans = []
current = 1  

for _ in range(n):
    num = int(input())

    while current <= num:
        stack.append(current)
        ans.append('+')
        current += 1

    if stack and stack[-1] == num:
        stack.pop()
        ans.append('-')
    else:
        print("NO")
        exit()

print(*ans, sep='\n')