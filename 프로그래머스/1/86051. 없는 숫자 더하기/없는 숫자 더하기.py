def solution(numbers):
    answer = list(range(10))
    answer = sum([i for i in answer if i not in {*numbers}])
    return answer