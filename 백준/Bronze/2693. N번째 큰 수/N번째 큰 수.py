# 제일 단순 무식하게 # 출력 모아뒀다가 한번에
import sys

def n_largest(array):
    return sorted(array, reverse= True)[2]

input = sys.stdin.readline
T = int(input())
ans = []
for _ in range(T):
    ans.append(n_largest(list(map(int, input().split()))))
for p in ans:
    print(p)