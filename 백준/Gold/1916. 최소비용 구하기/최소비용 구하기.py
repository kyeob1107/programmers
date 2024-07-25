# 다익스트라 알고리즘 찾아보고 사용 -> 왜 자꾸 2%대에서 틀리는지 모르겠음
# 이유 찾음 중복 노선 있을 경우 무조건 나중에 나온 노선의 값으로 계산해서 그럼, 그래서 수정했음2(더 괜찮은 방식 있는 듯해서 수정)
import sys
input = sys.stdin.readline
N = int(input().strip()) # 도시갯수
M = int(input().strip()) # 버스갯수

graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
init = float('inf') # 100_000 * M
cost = [init] * (N + 1)

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())

def get_smallest_city():
    min_val = init
    index = 0
    for i in range(1, N + 1):
        if cost[i] < min_val and not visited[i]:
            min_val = cost[i]
            index = i
    return index

def dijkstra(start):
    cost[start] = 0
    visited[start] = 1
    for route in graph[start]:
        if cost[route[0]] > route[1]:
            cost[route[0]] = route[1]
    
    for i in range(N - 1):
        now = get_smallest_city()
        visited[now] = 1
        for bus in graph[now]:
            cost_cal = cost[now] + bus[1]
            if cost_cal < cost[bus[0]]:
                cost[bus[0]] = cost_cal

if start == end:
    print(0)
else:
    dijkstra(start)
    print(cost[end])