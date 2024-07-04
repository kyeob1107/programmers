import sys
import itertools

def get_subsequences(seq):
    for r in range(1, len(seq) + 1):
        yield from itertools.combinations(seq, r)

input = sys.stdin.readline

N, S = map(int, input().split())
numbers = list(map(int, input().split()))

# 부분수열의 합이 S인 경우의 수를 계산
count = sum(1 for s in get_subsequences(numbers) if sum(s) == S)

print(count)