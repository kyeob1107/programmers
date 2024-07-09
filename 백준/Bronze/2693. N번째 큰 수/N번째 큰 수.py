# 제일 단순 무식하게 #출력도 바로바로
import sys

def n_largest(array):
    return sorted(array, reverse= True)[2]

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    print(n_largest(list(map(int, input().split()))))