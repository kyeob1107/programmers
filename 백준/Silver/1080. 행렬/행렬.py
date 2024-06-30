import sys
input = sys.stdin.readline

N, M = map(int, input().split())
matrix_a = []
matrix_b = []
check = [[0] * M for _ in range(N)]
for _ in range(N):
    matrix_a.append([int(i) for i in input().strip()])
for _ in range(N):
    matrix_b.append([int(i) for i in input().strip()])

for y in range(N):
    for x in range(M):
        if matrix_a[y][x] != matrix_b[y][x]:
            check[y][x] = 1
pos_range = [(-1, -1), (-1, 0), (-1, 1), 
             (0, -1), (0, 0), (0, 1),
             (1, -1), (1, 0), (1, 1)] # y, x
cnt = 0
if N < 3 and M < 3:
    if any(any(j==1 for j in check[i]) for i in range(N)):
        print(-1)
    
    else:
        print(0)
else:
    for y in range(1, N - 1):
        for x in range(1, M - 1):
            if check[y - 1][x - 1] == 1:
                cnt += 1
                for dy, dx in pos_range:
                    check[y + dy][x + dx] = (check[y + dy][x + dx] + 1)%2
    
    if any(any(j==1 for j in check[i]) for i in range(N)):
        cnt = -1
    print(cnt)