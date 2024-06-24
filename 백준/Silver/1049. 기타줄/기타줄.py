import sys
input = sys.stdin.readline


N, M = map(int, input().split())
six_prices = []
one_prices = []

for _ in range(M):
    six, one = map(int, input().split())
    six_prices.append(six)
    one_prices.append(one)
# six_prices, one_prices = map(list, zip(*(map(int, input().split()) for _ in range(M)))) #한줄로 하고 싶다면

six_min = min(six_prices)
one_min = min(one_prices)
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