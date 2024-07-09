import sys

def gcdlcm(a, b):
    if a > b: 
        c, d = a, b
    else: 
        c, d = b, a
    r = 1
    while r > 0:
        r = c%d
        c, d = d, r
    return c, int(a * b / c)

input = sys.stdin.readline
a, b =  map(int, input().split())
gcd, lcm = gcdlcm(a, b)
print(gcd)
print(lcm)