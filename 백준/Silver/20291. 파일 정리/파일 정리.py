import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
lst = []

for _ in range(N):
    file = input().strip()
    ans = file.split('.')[-1]
    lst.append(ans)

counter = Counter(lst)

for ans in sorted(counter):
    print(ans, counter[ans])