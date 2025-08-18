import sys

first = sys.stdin.readline().strip()

stack = []

for ch in first:
    if ch.isdigit():
        stack.append(int(ch))
    else:
        b = stack.pop()
        a = stack.pop()
        if ch == '+':
            stack.append(a + b)
        elif ch == '-':
            stack.append(a - b)
        elif ch == '*':
            stack.append(a * b)
        elif ch == '/':
            stack.append(int(a / b))

print(stack[-1])