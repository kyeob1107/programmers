# 뭔가 계산 단순화해서 가능할 듯해서 시도 , 바로 계산방식 2+
import sys
input = sys.stdin.readline
H, W = map(int, input().split())
height_arr = list(map(int, input().split()))
min_h =  min(height_arr)
res = 0

for standard in range(H, min_h, -1):
    temp = 0
    build = False
    for h in height_arr:
        if h >= standard:
            if not build:
                build = True
            else:
                res += temp
                temp = 0
        elif build:
            temp += 1
            
print(res)