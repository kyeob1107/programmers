def solution(n):
    if n==int(n**0.5)**2:
        return ((n**0.5)+1)**2
    else:
        return -1
#import math as m #math import 해도 되지만 내장으로만 하는게 더빠를듯해 제외
#print(int(16**0.5)) #float연산후 소수점제거 테스트
