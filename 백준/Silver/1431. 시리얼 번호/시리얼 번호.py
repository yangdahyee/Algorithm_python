import sys
input = sys.stdin.readline

N = int(input())
serial_list = []

for _ in range(N):
    serial = input().strip()

    s_sum = 0
    for ch in serial:
        if '0' <= ch <= '9':
            s_sum += int(ch)

    serial_list.append((len(serial), s_sum, serial))

serial_list.sort()

for item in serial_list:
    print(item[2])