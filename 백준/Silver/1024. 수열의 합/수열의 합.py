# 배열 만들어서

import sys

input = sys.stdin.readline

N, L = map(int, input().split())
s = sum([*range(L)])
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
        s = sum([*range(L)])

if N == (s + diff*L):
    print(*[i + diff for i in range(L)])