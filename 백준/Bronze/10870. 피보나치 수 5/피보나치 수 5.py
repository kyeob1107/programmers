import sys
input = sys.stdin.readline
n = int(input())
second = 0
first = 1
if n == 0: print(0)
elif n == 1: print(1)
else:
    for _ in range(n - 1):
        res = second + first
        second, first = first, res
    print(res)