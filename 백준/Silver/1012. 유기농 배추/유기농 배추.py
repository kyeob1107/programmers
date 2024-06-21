# 왜 빠른지 이해가 잘 안되서 그대로 해보는 코드 + row, col만 다른 방식으로
# 2등 코드
import sys

num = int(sys.stdin.readline())

move = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(x, y) :
    
    queue = [(x, y)]
    matrix[x][y] = 0 
    
    while queue :
        x, y = queue.pop(0)
        
        for dx, dy in move :
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m :
                continue
                
            if matrix[nx][ny] == 1 :
                queue.append((nx,ny))
                matrix[nx][ny] = 0

for i in range(num) :
    
    n, m, k = map(int, sys.stdin.readline().split())
    
    matrix = [[0] * m for i in range(n)]
    count = 0
    
    for i in range(k) :
        
        x, y = map(int, sys.stdin.readline().split())
        matrix[x][y] = 1
        
        
    for j in range(n) :
        for k in range(m) :
            if matrix[j][k] == 1:
                bfs(j, k)
                count += 1
    
    print(count)