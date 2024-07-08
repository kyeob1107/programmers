# 내장함수 이용
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    ans = bin(int(input()))
    for i, s in enumerate(ans[::-1][:-2]):
        if s == '1':
           print(i, end=' ') 