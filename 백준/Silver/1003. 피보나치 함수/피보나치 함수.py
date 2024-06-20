import sys

def fib(n):
    fibList=[1, 1]
    if n == 0:
        return 0
    elif n==1 or n==2:
        return 1
    for i in range(2,n):
        fibList.append( fibList[i-1] + fibList[i-2] )
        num=fibList[-1]
    return num

input = sys.stdin.readline
T = int(input())
for _  in range(T):
    N = int(input())
    if N == 0:
        print(1, end=' ')
        print(0)
        
    else:
        print(fib(N - 1), end=' ')
        print(fib(N))