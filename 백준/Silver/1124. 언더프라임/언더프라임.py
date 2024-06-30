# 뤼튼에게 개선 받아서 이해하고 다시 쓴 것 에라토스테네스 체 알고리즘 써서 소수리스트 구해서 그것 이용 방식
import sys
input = sys.stdin.readline

def sieve(max_num):
    is_prime = [1] * (max_num + 1)
    is_prime[0] = is_prime[1] = 0
    for i in range(2, int((max_num)**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max_num + 1, i):
                is_prime[j] = 0
    return [x for x in range(max_num + 1) if is_prime[x]]

def pm(n, primes):
    count = 0
    for prime in primes:
        if prime * prime > n:
            break
        while n % prime == 0:
            n //= prime
            count += 1
    if n > 1:  # n이 소수인 경우
        count += 1
    return count

A, B = map(int, input().split())
primes = sieve(int(B**0.5) + 1)
cnt = 0

for n in range(A, B + 1):
    num = pm(n, primes)
    if num != 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
        cnt += 1

print(cnt)