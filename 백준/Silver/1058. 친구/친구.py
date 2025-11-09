import sys
input = sys.stdin.readline

N = int(input())
friends = [input() for _ in range(N)] 

ans = 0
for i in range(N):
    cnt = 0
    for j in range(N):
        if i == j:
            continue
        if friends[i][j] == 'Y':
            cnt += 1
        else:
            for k in range(N):
                if friends[i][k] == 'Y' and friends[k][j] == 'Y':
                    cnt += 1
                    break
    if cnt > ans:
        ans = cnt

print(ans)