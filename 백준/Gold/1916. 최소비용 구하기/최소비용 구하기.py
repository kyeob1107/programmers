# 뤼튼이 알려준 다익스트라 알고리즘 우선순위 큐(힙)이용하는 방식 -> 왜 자꾸 2%대에서 틀리는지 모르겠음
# 이유 찾음 중복 노선 있을 경우 무조건 나중에 나온 노선의 값으로 계산해서 그럼, 
# 그래프 입력 방식 및 저장 방식 바꿔서
import heapq
import sys
input = sys.stdin.readline
N = int(input().strip()) # 도시갯수
M = int(input().strip()) # 버스갯수

graph = [dict() for node in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    if b in graph[a]:
        graph[a][b] = min(graph[a][b], c)
    else:
        graph[a][b] = c

start, end = map(int, input().split())

def dijkstra2(graph, start):
    distances = [float('inf')] * (N + 1)
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances


print(dijkstra2(graph, start)[end])