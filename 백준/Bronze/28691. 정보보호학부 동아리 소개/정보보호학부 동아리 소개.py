import sys
input = sys.stdin.readline

ch = input().strip()

clubs = {
    "M": "MatKor",
    "W": "WiCys",
    "C": "CyKor",
    "A": "AlKor",
    "$": "$clear"
}

print(clubs[ch])