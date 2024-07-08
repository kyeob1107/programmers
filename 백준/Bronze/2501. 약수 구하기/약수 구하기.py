import sys
input = sys.stdin.readline

N, K = map(int,input().split())
divisors = []
for i in range(1, N//2 + 1): 
    if N % i == 0 and i not in divisors:
        divisors.append(i)
        if i != N//i:
            divisors.append(N//i)

divisors.sort()
if K <= len(divisors):
    print(divisors[K - 1])
else:
    print(0)