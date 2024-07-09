import sys

def sieve(max_num):
    is_prime = [True] * (max_num + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int((max_num)**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max_num + 1, i):
                is_prime[j] = False
    return [x for x in range(max_num + 1) if is_prime[x]]

input = sys.stdin.readline

primes = sieve(1000)
N = int(input())
data = list(map(int, input().split()))
cnt = 0
for n in data:
    if n in primes:
        cnt += 1
print(cnt)