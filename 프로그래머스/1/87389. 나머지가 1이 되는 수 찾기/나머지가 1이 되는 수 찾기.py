def solution(n):
    for answer in range(1,n):
        if n%answer==1:
            return answer
        