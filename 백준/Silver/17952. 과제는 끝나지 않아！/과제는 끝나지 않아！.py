import sys
input = sys.stdin.readline

N = int(input())
stack = []
ans = 0

for _ in range(N):
    info = list(map(int, input().split()))
    
    if info[0] == 1:
        score, time = info[1], info[2]
        stack.append([score, time])
        
    if stack:
        stack[-1][1] -= 1
        
        if stack[-1][1] == 0:
            ans += stack[-1][0]
            stack.pop()
            
print(ans)
