import sys
input = sys.stdin.readline

minguk = sum(map(int, input().split()))
manse = sum(map(int, input().split()))

print(max(minguk, manse))