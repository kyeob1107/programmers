import sys
input = sys.stdin.readline

N = int(input())
info = map(int, input().split())
line = [0] * N
indexing = list(range(N))
for i, p in enumerate(info):
    height = i + 1
    line[indexing[p]] =  height
    indexing.remove(indexing[p])
print(*line)