import sys
input = sys.stdin.readline

N = int(input())
members = []

for i in range(N):
    age, name = input().split()
    age = int(age)
    members.append((age, name))
    
members.sort(key=lambda x: x[0])

for age, name in members:
    print(age, name)
