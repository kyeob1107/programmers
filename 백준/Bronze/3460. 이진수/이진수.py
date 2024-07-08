# 2진수 아예 내장함수 안 쓰고 구현
import sys

def con_n_not_builtin(n,q): #n진법 변환기 (conversion to base n)
    rev_base = ''

    while n > 0:
        n, mod = n//q, n%q
        rev_base += str(mod)

    return rev_base[::-1]

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    ans = con_n_not_builtin(int(input()), 2)
    for i, s in enumerate(ans[::-1]):
        if s == '1':
           print(i, end=' ')