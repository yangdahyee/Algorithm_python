import sys
input = sys.stdin.readline

S = input().rstrip()
bomb = input().rstrip()
b_len = len(bomb)

stack = []

for ch in S:
    stack.append(ch)
    if ch == bomb[-1]:
        if stack[-b_len:] == list(bomb):
            del stack[-b_len:]
            
print(''.join(stack) or 'FRULA')