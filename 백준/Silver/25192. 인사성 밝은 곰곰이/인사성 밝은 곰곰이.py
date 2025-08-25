import sys
input = sys.stdin.readline

N = int(input())
gomgom_check = set()
cnt = 0

for _ in range(N):
    user = input().strip()
    
    if user == "ENTER":
        gomgom_check.clear()
        
    else: 
        if user not in gomgom_check:
            cnt += 1
            gomgom_check.add(user)

print(cnt)