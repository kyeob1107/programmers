import sys
from collections import deque
input = sys.stdin.readline

def bfs(start_x, start_y):
    move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(start_x, start_y)])
    positions.remove((start_x, start_y))
    
    while queue:
        x, y = queue.popleft()
        for dx, dy in move:
            nx, ny = x + dx, y + dy
            if (nx, ny) in positions:
                positions.remove((nx, ny))
                queue.append((nx, ny))

T = int(input().strip())
results = []

for _ in range(T):
    M, N, K = map(int, input().strip().split())
    positions = set()
    
    for _ in range(K):
        X, Y = map(int, input().strip().split())
        positions.add((X, Y))

    cnt = 0
    while positions:  # positions이 비어질 때까지 반복
        px, py = next(iter(positions))  # positions의 임의의 요소 하나 가져오기
        bfs(px, py)
        cnt += 1
    
    results.append(cnt)

for result in results:
    print(result)
