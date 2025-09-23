import sys
input = sys.stdin.readline

check = set()

N = int(input())
for _ in range(N):
        name, log = input().split()
        if log == "enter":
            check.add(name)
        else:
            check.remove(name)

for name in sorted(check, reverse=True):
    print(name)