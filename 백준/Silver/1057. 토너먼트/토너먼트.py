import sys
input = sys.stdin.readline

N, num_1, num_2 = map(int, input().split())
rnd = 0
while N>=1 :
    if num_1 == num_2:
        break
    num_1 = (num_1 + 1)//2
    num_2 = (num_2 + 1)//2
    N //= 2
    rnd += 1

print(rnd)