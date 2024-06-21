import sys
import math
input = sys.stdin.readline

T = int(input())
ans = []
for _ in range(T):
    a, b = map(int, input().split())
    ans.append(math.comb(b, a))
for a in ans:
    print(a)