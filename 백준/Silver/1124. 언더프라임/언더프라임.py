# 뤼튼이 개선 해준 코드
import sys
import math

def sieve(max_num):
    is_prime = [True] * (max_num + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(math.sqrt(max_num)) + 1):
        if is_prime[i]:
            for j in range(i * i, max_num + 1, i):
                is_prime[j] = False
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

input = sys.stdin.read

def main():
    data = input()
    A, B = map(int, data.split())
    max_num = B
    primes = sieve(int(math.sqrt(max_num)) + 1)
    cnt = 0

    for n in range(A, B + 1):
        num = pm(n, primes)
        if num != 1 and all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1)):
            cnt += 1

    print(cnt)

if __name__ == "__main__":
    main()