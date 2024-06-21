import sys
input = sys.stdin.readline
N, M = map(int, input().split())

case1 = [[False if (i + j) % 2 == 0 else True for j in range(M)] for i in range(N)]
case2 = [[True if (i + j) % 2 == 0 else False for j in range(M)] for i in range(N)]

check1 = [[0]*M for _ in range(N)]
check2 = [[0]*M for _ in range(N)]

# 백 False, 흑 True 로
board = [[False if s == 'W' else True for s in input().strip()] for _ in range(N)]

if board == case1 or board == case2:
    print(0)

else:
    for y in range(N):
        for x in range(M):
            if board[y][x] == case1[y][x]:
                check2[y][x] = 1
            else:
                check1[y][x] = 1
    ans = N * M
    for start_pos_y in range(N - 7):
        for start_pos_x in range(M - 7):
            temp = min(sum(sum(row[start_pos_x:start_pos_x+8]) for row in check1[start_pos_y:start_pos_y+8]), 
                      sum(sum(row[start_pos_x:start_pos_x+8]) for row in check2[start_pos_y:start_pos_y+8]))
            # print(start_pos_y, start_pos_x, temp)
            if ans > temp:
                ans = temp

    print(ans)