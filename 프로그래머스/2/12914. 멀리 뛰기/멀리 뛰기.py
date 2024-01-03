def fib(n):
    fibList=[1, 1]
    if n==1 or n==2:
        return 1
    for i in range(2,n):
        fibList.append( fibList[i-1] + fibList[i-2] )
        num=fibList[-1]
    return num

def solution(n):
    answer = 0
    answer=fib(n+1)%1234567
    return answer


'''def nCm(n,m):
    num=1
    for i in range(1,m+1):
        num=num*(n-i+1)/i
    return int(num)
def solution(n):
    answer = 0
    m=n//2 #0이 아닌 계산상 계산하면 되는 범위관련
    for i in range(m+1):
        answer+=(nCm(n-i,i)%1234567)
        
    return answer%1234567'''
