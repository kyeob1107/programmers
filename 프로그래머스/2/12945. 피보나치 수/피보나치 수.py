def fib(n): #피보나치 수열 함수 (메모이제이션 방식) 빠르진 않을 듯
    fibList=[1, 1]
    if n==1 or n==2:
        return 1
    for i in range(2,n):
        fibList.append( fibList[i-1] + fibList[i-2] )
        num=fibList[-1]
    return num

def solution(n):
    return fib(n)%1234567