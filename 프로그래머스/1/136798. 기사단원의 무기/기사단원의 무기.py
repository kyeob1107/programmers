def divisors(num): #약수의 갯수를 리턴해주는 함수
    count=0
    for i in range(1,int(num ** 0.5)+1): #제곱근한 값의 이전까지 체크
        if num/i==i:
            count+=1
        elif num % i ==0:
            count+=2
    return count

def solution(number, limit, power):
    answer = 0
    for i in range(1,number+1):
        if divisors(i)<=limit: #제한 수치보다 작거나 같은 무기
            answer+=divisors(i)
        else: #제한 수치보다 큰 무기
            answer+=power
    return answer