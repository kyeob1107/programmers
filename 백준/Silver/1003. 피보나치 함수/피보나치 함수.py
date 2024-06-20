import sys

def multiply(a, b, x, y):
    return x*(a+b) + a*y, a*x + b*y

def square(a, b):
    a2 = a * a
    b2 = b * b
    ab = a * b
    return a2 + (ab << 1), a2 + b2

def power(a, b, m):
    if m == 0:
        return (0, 1)
    elif m == 1:
        return (a, b)
    else:
        x, y = a, b
        n = 2
        while n <= m:
            # repeated square until n = 2^q > m
            x, y = square(x, y)
            n = n*2
        # add on the remainder
        a, b = power(a, b, m-n//2)
        return multiply(x, y, a, b)

def implicit_fib(n):
    a, b = power(1, 0, n)
    return a

input = sys.stdin.readline
T = int(input())
for _  in range(T):
    N = int(input())
    if N == 0:
        print(1, end=' ')
        print(0)
    # cnt_0 = cnt_1 = 0
    else:
        print(implicit_fib(N - 1), end=' ')
        print(implicit_fib(N))