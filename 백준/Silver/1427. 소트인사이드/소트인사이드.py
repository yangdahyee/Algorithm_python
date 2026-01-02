import sys
input = sys.stdin.readline

N = input().strip()
ans = sorted(N)[::-1]
print(''.join(ans))