def comb(n, r):
    result = 1
    for i in range(1, r + 1):
        result *= n
        result //= i
        n -= 1
    return result

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(comb(M, N))
    
    