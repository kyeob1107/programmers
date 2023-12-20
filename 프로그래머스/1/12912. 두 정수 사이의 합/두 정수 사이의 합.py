def solution(a, b):
    answer = 0
    if a<=b:
        for i in range(a,b+1):
            answer+=i
    else :
        for i in range(b,a+1):
            answer+=i
    return answer

#import numpy as np쓰면 linspce로 더 간편하나 더 빠르게하고 싶어 내장함수로
#간단히만 했는데 속도 좀 걸려서 줄일 수 있으면 좋을듯