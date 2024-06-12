# dfs
from sys import stdin

input = stdin.readline

def dfs(s):
    visited[s-1] = True
    infection_list.append(s)
    for com in adj_list[s-1]:
        if not visited[com-1]:
            dfs(com)
        

N = int(input())
M = int(input())

infection_list = []
visited = [False] * N
adj_list =[[] for _ in range(N)]


for _ in range(M):
    a, b = map(int, input().split())
    adj_list[a - 1].append(b)
    adj_list[b - 1].append(a)

dfs(1)
print(len(infection_list)-1)