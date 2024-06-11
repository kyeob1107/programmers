from sys import stdin as s
from collections import deque

line_data = []
nodes_list = deque()
answer = []
answer2 = []
# 읽어오는 부분
#s = open("input1260.txt","rt") #절대 경로도 되고, 상대 경로도 된다.
                         # r read t text 

n, m, v = map(int, s.readline().split())
for i in range(m):
    start, end = map(int,s.readline().split())
    line_data.append([start, end]) # [[1, 2], [1, 3], [1, 4], [2, 4], [3, 4]]

# dfs
nodes_list.append(v)
while nodes_list:
    node = nodes_list.pop()
    
    if node not in answer:
        answer.append(node)
        need_nodes=[]
        
        for elem in line_data:
            if node in elem:
                for value in elem:
                    if value != node:
                        need_nodes.append(value)
        need_nodes.sort(reverse=True)
        nodes_list.extend(need_nodes)

for i in answer:
    print(i, end=" ")
print()

# bfs
nodes_list.append(v)
while nodes_list:
    node = nodes_list.popleft()
    
    if node not in answer2:
        answer2.append(node)
        need_nodes=[]
        
        for elem in line_data:
            if node in elem:
                for value in elem:
                    if value != node:
                        need_nodes.append(value)
        need_nodes.sort()
        nodes_list.extend(need_nodes)

for i in answer2:
    print(i, end=" ")