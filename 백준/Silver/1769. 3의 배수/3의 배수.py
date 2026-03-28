import sys
input = sys.stdin.readline

s = input().strip()
c = 0

while len(s) > 1:
    c += 1
    s = str(sum(map(int, s)))

print(c)
print("YES" if int(s) % 3 == 0 else "NO")