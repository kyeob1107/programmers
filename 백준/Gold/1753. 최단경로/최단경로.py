# 함수부분 그냥 결과 저장하고 저장 결과 가져다 쓰기
import heapq
import sys
input = sys.stdin.readline
V, E = map(int, input().split()) # 정점, 간선
start = int(input().strip())
graph = [{} for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    if v in graph[u]:
        graph[u][v] = min(graph[u][v], w)
    else:
        graph[u][v] = w

init = float('inf')

def dijkstra(graph, start):
    distances = [init] * (V + 1)
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

distances = dijkstra(graph, start)
for i in range(1, V + 1):
    if distances[i] == init:
        print("INF")
    else:
        print(distances[i])