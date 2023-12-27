def prime_num(num): #해당 주어진 수가 소수인지 아닌지 판별하는 함수
    for i in range(2, int(num**0.5)+1): # n의 제곱근을 정수화 시켜준 후 + 1
        if num % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j+1,len(nums)):
                if prime_num(nums[i]+nums[j]+nums[k]) :
                    answer+=1
    return answer