L, P = map(int, input().split())
news = list(map(int, input().split()))

check = L * P

for i in news:
    print(i - check, end=' ')