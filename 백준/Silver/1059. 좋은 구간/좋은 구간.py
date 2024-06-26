import sys
input = sys.stdin.readline

def good_section(S, n):
    if n in S:
        return 0
    under = max([s for s in S if s < n] + [0]) + 1
    upper = min([s for s in S if s > n] + [1001]) - 1
    return (n - under) * (upper - n + 1) + (upper - n)

L =int(input())
S = list(map(int, input().split()))
n = int(input())

print(good_section(S, n))