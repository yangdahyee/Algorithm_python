import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [input().strip() for _ in range(N)]

cnt = 0

for i in range(N):
    for j in range(M):
        if board[i][j] == '-':
            if j == 0 or board[i][j-1] != '-':
                cnt += 1
        else: 
            if i == 0 or board[i-1][j] != '|':
                cnt += 1

print(cnt)