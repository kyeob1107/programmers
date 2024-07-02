# 미리 다 입력 기록해두고 하는 방식
import sys
input = sys.stdin.readline

N = int(input())
info = [list(map(int, input().split())) for _ in range(N)]
cal_cost = [0, 0, 0]
for i in range(N - 1):
    cal_cost[0] = min(info[i][1] + info[i + 1][0], info[i][2] + info[i + 1][0])
    cal_cost[1] = min(info[i][0] + info[i + 1][1], info[i][2] + info[i + 1][1])
    cal_cost[2] = min(info[i][1] + info[i + 1][2], info[i][0] + info[i + 1][2])
    info[i + 1] = cal_cost.copy() # 주의! 그냥 같다하면 메모리 주소가 복사됨

print(min(info[-1]))