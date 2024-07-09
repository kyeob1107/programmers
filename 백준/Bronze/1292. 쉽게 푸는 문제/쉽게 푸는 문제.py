# 수학적으로 바로 계산해보려는 것, 추가로 정리해서 해보는 것
import sys

def sum_n(n):
    return n * (n + 1) //2

def sum_square(n):
    return n * (n + 1) * (2*n + 1) //6

input = sys.stdin.readline

A, B = map(int, input().split())

a_check = True
for n in range(1, 46):
    if sum_n(n) >= A and a_check:
        a_n = n
        a_check = False
    if sum_n(n) >= B:
        b_n = n
        break

print(sum_square(b_n) - sum_square(a_n) - (sum_n(b_n) - B) * b_n + (sum_n(a_n) - A + 1) * a_n)