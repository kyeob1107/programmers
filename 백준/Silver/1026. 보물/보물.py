import sys
input = sys.stdin.readline
N = int(input())
A = sorted(map(int, input().split()), reverse = True)
B = sorted(map(int, input().split()))

print(sum(x*y for x, y in zip(A, B)))