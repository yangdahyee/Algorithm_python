import sys
input = sys.stdin.readline

M = int(input())
S = set()

for _ in range(M):
    cmd = input().split()

    if cmd[0] == "all":
        S = set(range(1, 21))

    elif cmd[0] == "empty":
        S.clear()

    else:
        num = int(cmd[1])

        if cmd[0] == "add":
            S.add(num)

        elif cmd[0] == "remove":
            S.discard(num)

        elif cmd[0] == "check":
            print(1 if num in S else 0)

        elif cmd[0] == "toggle":
            if num in S:
                S.remove(num)
            else:
                S.add(num)