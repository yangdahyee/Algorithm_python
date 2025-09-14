import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    candidates = [list(map(int, input().split())) for _ in range(N)]
    
    candidates.sort()
    
    cnt = 1
    check_interview = candidates[0][1]
    
    for i in range(1, N):
        interview = candidates[i][1]
        if interview < check_interview:
            cnt += 1
            check_interview = interview
    
    print(cnt)