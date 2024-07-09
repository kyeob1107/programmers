import sys
input = sys.stdin.readline

data = sorted([int(input()) for _ in range(9)])

total = sum(data)
switch = False
for i in range(9):
    for j in range(i + 1, 9):
        if (total - 100) == (data[i] + data[j]):
            for index, p in enumerate(data):
                if index not in [i, j]:
                    print(p)
            switch = True
            break
    if switch:
        break