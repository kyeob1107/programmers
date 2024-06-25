import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
rectangle = []
selections = dict()
for i in range(N):
    row_temp = [int(n) for n in input().strip()]
    rectangle.append(row_temp)
    for j, val in enumerate(row_temp):
        if val not in selections:
            selections[val] = [(i, j)]
        else:
            selections[val].append((i, j))

selections = {k: v for k, v in selections.items() if len(v)>3}
ans = 1
max_len = min(N, M)
for positions in selections.values():
    for pos in positions:
        row, col = pos
        for r in range(1, max_len):
            if (row + r, col) in positions:
                if (row, col + r) in positions and (row + r, col + r) in positions:
                    ans = max(ans, r + 1)
print(ans**2)