import sys

def sieve(max_num):
    is_prime = [True] * (max_num + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(max_num ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max_num + 1, i):
                is_prime[j] = False
    return [x for x in range(2, max_num + 1) if is_prime[x]]

input = sys.stdin.readline

M = int(input())
N = int(input())
primes = [x for x in sieve(N) if x >= M and x <= N]
if primes:
    print(sum(primes))
    print(primes[0])
else:
    print(-1)