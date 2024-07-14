import sys
input = sys.stdin.readline
H, W = map(int, input().split())
height_arr = list(map(int, input().split()))

graph = [[1 if H - i <= height_arr[j] else 0 for j in range(W)] for i in range(H)] # H 관련해서는 최소 ~ 최대 만큼만 갯수 하면 될듯

for h in range(H):
    if sum(graph[h]) >= 2: # (h == 0 or not (2 in graph[h-1])) and
        wall_index = [i for i in range(W) if graph[h][i] == 1]
        for start, end in zip(wall_index, wall_index[1:]):
            graph[h][start + 1: end] = [2] * (end - start - 1)
            
print(sum(row.count(2) for row in graph))