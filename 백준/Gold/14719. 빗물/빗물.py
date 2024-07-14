# 뭔가 계산 단순화해서 가능할 듯해서 시도 , 인덱스 저장하고 계산방식 2
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
        if not build and h >= standard:
            build = True
        elif build and h < standard:
            temp += 1
        elif build and h >= standard:
            res += temp
            temp = 0

print(res)