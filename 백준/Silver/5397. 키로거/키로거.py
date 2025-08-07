import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    text = input().rstrip()
    
    left = []
    right = []
    
    for char in text:
        if char == '-':
            if left:
                left.pop()
        
        elif char == '<':
            if left:
                right.append(left.pop())
                
        elif char == '>':
            if right:
                left.append(right.pop())
        else:
            left.append(char)

    print(''.join(left + right[::-1]))