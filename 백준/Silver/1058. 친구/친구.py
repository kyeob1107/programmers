import sys
input = sys.stdin.readline
        
N = int(input())
graph = []
for _ in range(N):
    graph.append([0 if s=='N' else 1 for s in input().strip()])

max_f = 0
for p_n in graph:
    cnt = 0
    friends = p_n.copy()
    plus_f = [i for i, c in enumerate(p_n) if c]
    for i in plus_f:
        for j in range(N):
            if graph[i][j]:
                friends[j] = 1
    cnt = friends.count(1) - 1
    max_f = max(cnt, max_f)
print(max_f)