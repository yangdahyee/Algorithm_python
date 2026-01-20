import sys
input = sys.stdin.readline

A, B = map(int, input().split())

a, b = A, B
while b:
    a, b = b, a % b

print((A // a) * B)