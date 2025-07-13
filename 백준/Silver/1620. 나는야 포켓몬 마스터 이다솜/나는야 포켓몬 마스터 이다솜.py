import sys
input = sys.stdin.readline

N, M = map(int, input().split())
pokedex = {}

for i in range(1, N + 1):
    name = input().strip()
    pokedex[name] = i
    pokedex[i] = name

for _ in range(M):
    query = input().strip()
    
    if query.isdigit():
        print(pokedex[int(query)])
    else:
        print(pokedex[query])