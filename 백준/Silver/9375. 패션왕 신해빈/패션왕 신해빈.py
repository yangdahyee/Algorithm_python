import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):  
    N = int(input())    
    clothes = {}
    
    for _ in range(N):
        name, style = input().split()
        if style not in clothes:
            clothes[style] = 1
        else:
            clothes[style] += 1
        
    ans = 1
    for style in clothes:
        ans *= (clothes[style] + 1) 
    ans -= 1
    
    print(ans)