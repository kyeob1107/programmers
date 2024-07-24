# 레퍼런스
from collections import deque
import sys

input = sys.stdin.readline

N, M = int(input()), int(input())
arr = [list(map(int, input().strip().split())) for _ in range(M)]
graph = [[-1] * (N+1) for _ in range(N+1)]
for i, j, cost in arr:
    if graph[i][j] == -1 or graph[i][j] > cost:
        graph[i][j] = cost

visit = [False] * (N+1)
distance = [0] * (N+1)
q = deque()
start, end = list(map(int, input().strip().split()))
q.append(start)
visit[start] = True
while q:
    now = q.popleft()
    for i, cost in enumerate(graph[now]):
        if cost > -1 and (not visit[i] or (visit[i] and distance[i] > distance[now] + cost)):
            q.append(i)
            visit[i] = True
            distance[i] = distance[now] + cost

print(distance[end])