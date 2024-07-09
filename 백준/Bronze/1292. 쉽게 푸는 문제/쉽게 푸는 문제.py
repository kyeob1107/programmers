# 단순 무식하게
import sys
input = sys.stdin.readline

A, B = map(int, input().split())

series = []
for i in range(int((2*B)**0.5 + 1) + 1):
    series += [i] * i
print(sum(series[A-1:B]))