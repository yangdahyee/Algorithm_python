import sys
input = sys.stdin.readline

board = input().strip()

ans = board.replace("XXXX", "AAAA")
ans = ans.replace("XX", "BB")

if "X" in ans:
    print(-1)
else:
    print(ans)
