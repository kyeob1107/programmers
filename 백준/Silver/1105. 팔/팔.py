# 뤼튼보고 개선시켜보라고 한 것(추가로 내가 살짝 손봄)
import sys
input = sys.stdin.readline

L, R = input().split()
cnt = 0

if len(L) == len(R):
    for l, r in zip(L, R):
        if l != r:
            break
        elif l == '8':
            cnt += 1

print(cnt)