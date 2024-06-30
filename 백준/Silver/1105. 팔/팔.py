# 문자열로 쓴 방식
import sys
input = sys.stdin.readline

L, R = input().split()
cnt = 0

if len(L) == len(R):
    L_num = [s for s in L]
    R_num = [s for s in R]
    for l, r in zip(L_num, R_num):
        if l == r:
            if l == '8':
                cnt +=1
        else:
            break
print(cnt)