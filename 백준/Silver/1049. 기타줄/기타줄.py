import sys
input = sys.stdin.readline

N, M = map(int, input().split())
min_package = float('inf')
min_single = float('inf')

for _ in range(M):
    package, single = map(int, input().split())
    min_package = min(min_package, package)
    min_single = min(min_single, single)

all_single = N * min_single
all_package = ((N + 5) // 6) * min_package
mix = (N // 6) * min_package + (N % 6) * min_single

ans = min(all_single, all_package, mix)
print(ans)