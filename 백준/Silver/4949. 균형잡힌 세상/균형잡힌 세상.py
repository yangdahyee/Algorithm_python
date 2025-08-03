import sys
input = sys.stdin.readline 

while True:
    text = input().rstrip()
    if text == ".":
        break
    
    stack = []
    
    for char in text:
        if char == "(" or char == "[":
            stack.append(char)
        elif char == ")":
            if stack and stack[-1]== "(":
                stack.pop()
            else:
                print("no")
                break 
        elif char == "]":
            if stack and stack[-1]== "[":
                stack.pop()
            else:
                print("no")
                break 
    else:
        if not stack:
            print("yes")
        else:
            print("no")