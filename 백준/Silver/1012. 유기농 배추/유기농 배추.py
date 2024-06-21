import sys
from collections import deque
input = sys.stdin.readline

def bfs(i, j):
    move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(j, i)])
    while queue:
        x, y = queue.popleft()
        if (x, y) in visited:
            continue
        visited.add((x, y))
        for dx, dy in move:
            nx = x + dx
            ny = y + dy
            if (nx, ny) in positions and (nx, ny) not in visited:
                queue.append((nx, ny))

T = int(input())
ans = []
for _ in range(T):
    M, N, K = map(int, input().split())
    visited = set()
    positions = set()
    cnt = 0
    for _ in range(K):
        X, Y = map(int, input().split())
        positions.add((X, Y))
    
    for x, y in positions:
        if (x, y) not in visited:
            bfs(y, x)
            cnt += 1
    ans.append(cnt)

for a in ans:
    print(a)