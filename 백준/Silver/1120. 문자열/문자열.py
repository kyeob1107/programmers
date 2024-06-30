# 제일 먼저 단순무식하게
import sys
input = sys.stdin.readline

A, B = input().split()
la = len(A)
lb = len(B)
dif = len(A)
for i in range(lb - la + 1):
    cnt = 0
    for sa, sb in zip(A, B[i:i + la]):
        if sa != sb:
            cnt += 1
    dif = min(dif, cnt)
print(dif)