# 입력버퍼 하나씩 가져와서 이용하고 그 다음 가지고 오고 하는 방식
import sys
input = sys.stdin.readline

N = int(input())
pre_house, cal_cost = [0, 0, 0], [0, 0, 0]
for _ in range(N):
    input_data = list(map(int, input().split()))
    cal_cost[0] = min(pre_house[1] + input_data[0], pre_house[2] + input_data[0])
    cal_cost[1] = min(pre_house[0] + input_data[1], pre_house[2] + input_data[1])
    cal_cost[2] = min(pre_house[1] + input_data[2], pre_house[0] + input_data[2])
    pre_house = cal_cost.copy() # 주의! 그냥 같다하면 메모리 주소가 복사됨
print(min(pre_house))