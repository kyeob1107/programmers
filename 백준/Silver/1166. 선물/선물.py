# 제대로 이해도 안가고 이진탐색 아직 어색해서 검색해서 한번 보고 안보고나서 작성해본 것
import sys
input = sys.stdin.readline

N, L, W, H = map(int, input().split())
start, end = 0, max(L, W, H)

for i in range(100):
    mid = (start + end) / 2
    if (L//mid) * (W//mid) * (H//mid) < N:
        end = mid
    else:
        start = mid
print(mid)