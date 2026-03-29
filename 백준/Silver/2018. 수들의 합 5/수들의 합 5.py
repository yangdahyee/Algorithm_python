N = int(input())

s = 1
e = 1
sum_n = 1
cnt = 0

while s <= N:
    if sum_n < N:
        e += 1
        sum_n += e
    elif sum_n > N:
        sum_n -= s
        s += 1
    else:
        cnt += 1
        sum_n -= s
        s += 1

print(cnt)