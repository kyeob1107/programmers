def solution(left, right):
    answer=0
    for num in range(left,right+1):
        if len([i for i in range(1, (num // 2) + 1) if num % i == 0]+[num]) %2 ==1: #전체 약수 구하는 리스트 만드는 코드의 길이 확인
            answer-=num
        else:
            answer+=num     
    return answer