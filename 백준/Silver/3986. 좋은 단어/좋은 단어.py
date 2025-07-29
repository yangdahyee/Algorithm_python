import sys
input = sys.stdin.readline

N = int(input())
cnt = 0

for _ in range(N):
    word = input().strip()
    stack = []
    
    for char in word:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
            
    if not stack:
        cnt += 1
        
print(cnt)