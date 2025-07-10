import sys

check = sys.stdin.readline().strip()
check_idx = 0
N = 1

while True:
    for ch in str(N):
        if check_idx < len(check) and ch == check[check_idx]:
            check_idx += 1
            if check_idx == len(check):
                print(N)
                sys.exit()
    N += 1