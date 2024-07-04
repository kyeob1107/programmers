import sys
import itertools

def get_subsequences(seq):
    subsequences = []
    for r in range(len(seq) + 1):
        subsequences.extend(itertools.combinations(seq, r))
    return subsequences

input = sys.stdin.readline

N, S = map(int, input().split())
numbers = list(map(int, input().split()))
print(sum(1 for s in get_subsequences(numbers) if len(s)!=0 and sum(s) == S))