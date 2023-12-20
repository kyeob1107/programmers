def solution(n):
    return int(''.join(list(reversed(sorted(list(str(n)))))))


#정렬 내림차순으로 바로 할방법도 있었을듯한데 기억X,
#바로 찾지못하여 빠르게 푸느라 번거롭더라도 저렇게 하였음
#보기편하게 변수를 지정하여 보여주면 다음과 같음
'''list_n=list(str(n))
    rev_n=list(reversed(sorted(list_n)))
    answer = int(''.join(rev_n))
    #print(answer)
    return answer'''