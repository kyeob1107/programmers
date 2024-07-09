# 수학적으로 바로 계산해보려는 것 일단 정리 바로 안되서 프로토타입
import sys

def sum_square(n):
    return n * (n + 1) * (2*n + 1) //6

input = sys.stdin.readline

A, B = map(int, input().split())
# 최대 1000까지면 45까지 등장함
number = [n * (n + 1) //2 for n in range(1, 46)]
# print(number)
a_check = True
for num in range(len(number)):
    if number[num] >= A and a_check:
        a_n = num + 1
        a_check = False
    if number[num] >= B:
        b_n = num + 1
        break
# print(a_n, b_n)
# print(sum_square(b_n), sum_square(a_n), (number[b_n - 1] - B) * b_n, (number[a_n - 1] - A + 1) * a_n)
print(sum_square(b_n) - sum_square(a_n) - (number[b_n - 1] - B) * b_n + (number[a_n - 1] - A + 1) * a_n)