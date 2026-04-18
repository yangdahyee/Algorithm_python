import sys
input = sys.stdin.readline

while True:
    name, age, weight = input().split()
    
    if name == "#":
        break
    
    age = int(age)
    weight = int(weight)
    
    if age > 17 or weight >= 80:
        ans = "Senior"
    else:
        ans = "Junior"
    
    print(name, ans)