def solution(n, left, right):
    answer = []    
    answer=[0 for i in range(right-left+1)]
    for i in range(len(answer)):
        answer[i]+= 1+max((left+i)//n,(left+i)%n)
        #x,y중 큰 것 값따라 추가계산

    return answer