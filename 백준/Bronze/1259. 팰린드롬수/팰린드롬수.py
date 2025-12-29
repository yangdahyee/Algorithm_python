
while True:
    num = input()
    if num == "0":
        break
    b = num[::-1]
    if num == b:
        print("yes")
    else:
        print("no")