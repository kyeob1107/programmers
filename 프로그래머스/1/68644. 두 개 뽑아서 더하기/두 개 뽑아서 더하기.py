def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            if numbers[i]+numbers[j] not in answer: #이미 안에 있는지 확인
                answer.append(numbers[i]+numbers[j])
    answer.sort()
    return answer
'''def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            if numbers[i]+numbers[j] not in answer: #이미 안에 있는지 확인
                answer.append(numbers[i]+numbers[j])
    answer.sort()
    return answer'''