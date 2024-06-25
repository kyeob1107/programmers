import sys
input = sys.stdin.readline

N, M = map(int, input().split())
rectangle = [[] for _ in range(10)]
for i in range(N):
    row_temp = [int(n) for n in input().strip()]
    for j, val in enumerate(row_temp):
        rectangle[val%10].append((i, j))

ans = 1
max_len = min(N, M)
for positions in rectangle:
    if len(positions) < 4:
        continue
    
    for pos in positions:
        row, col = pos
        for r in range(max_len, 0, -1):
            if (row + r, col) in positions:
                if (row, col + r) in positions and (row + r, col + r) in positions:
                    ans = max(ans, r + 1)
                    break
print(ans**2)