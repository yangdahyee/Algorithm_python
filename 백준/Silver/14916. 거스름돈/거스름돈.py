import sys
input = sys.stdin.readline

n = int(input())
five_cnt = n // 5
rest_coin = n % 5

while True:
    if five_cnt < 0:
        print(-1)
        break
    if rest_coin % 2 == 0:
        print(five_cnt + (rest_coin // 2))
        break

    five_cnt -= 1
    rest_coin += 5
