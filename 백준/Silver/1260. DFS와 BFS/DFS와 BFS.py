from sys import stdin

input = stdin.readline

def dfs(s):
    visited[s-1] = True
    dfs_list.append(s)
    for e in sorted(adj_list[s-1]):
        if not visited[e-1]:
            dfs(e)
            
def bfs(s):
    visited[s-1] = True
    queue = [s]
    while queue:
        v = queue.pop(0)
        bfs_list.append(v)
        for e in sorted(adj_list[v-1]):
            if not visited[e-1]:
                visited[e-1] = True
                queue.append(e)
    
N, M, V = map(int, input().split())
adj_list = [[] for _ in range(N)]
visited = [False] * (N)

for _ in range(M):
    a, b = map(int, input().split())
    adj_list[a - 1].append(b)
    adj_list[b - 1].append(a)

dfs_list = []
bfs_list = []

dfs(V)
visited = [False] * (N)
bfs(V)

print(*dfs_list)
print(*bfs_list)