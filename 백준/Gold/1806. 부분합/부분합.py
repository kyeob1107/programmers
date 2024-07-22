# 뤼튼이 제시해준 투 포인트 기법 - 아마 이대로는 문제 생길듯
import sys
input = sys.stdin.readline
N, S = map(int, input().split())
series = list(map(int, input().split()))

res = float('inf')
left = 0
current_sum = 0

for right in range(N):
    current_sum += series[right]
    while current_sum >= S:
        res = min(res, right - left + 1)
        current_sum -= series[left]
        left += 1

if res == float('inf'):
    print(0)
else:
    print(res)