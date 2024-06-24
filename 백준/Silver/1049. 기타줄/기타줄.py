import sys
input = sys.stdin.readline

N, M = map(int, input().split())

six_min = 1000
one_min = 1000

for _ in range(M):
    six, one = map(int, input().split())
    six_min = min(six, six_min)
    one_min = min(one, one_min)
    

money = 0

if six_min > one_min * 6:
    money += N * one_min

else:
    money += (N // 6) * six_min
    
    if six_min > one_min * (N % 6):
        money += one_min * (N % 6)
        
    else:
        money += six_min

print(money)