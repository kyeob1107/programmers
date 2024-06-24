# 배열 만들어서 합 구하는 방식 변경

import sys

input = sys.stdin.readline

N, L = map(int, input().split())
s = (L-1) * L //2
diff = 0

while N != s :
    if N < s or L > 100:
        print(-1)
        break
    
    elif (N - s)%L==0:
        diff = (N - s)//L
        break
        
    else:
        L += 1
        s = (L-1) * L //2

if N == (s + diff*L):
    print(*[i + diff for i in range(L)])