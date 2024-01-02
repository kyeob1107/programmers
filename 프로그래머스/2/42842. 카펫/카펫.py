def divisors_list(num): #약수들의 리스트인데 살짝 손봐서 제곱수의 제곱근포함한 절반 이하만
    if num==1:
        return [1]
    return [i for i in range(1, (num // 2) + 1) if num % i == 0 and num//i >= i]

def solution(brown, yellow):
    n=0 #가로 길이
    m=0 #세로 길이
    #(n-2)+(m-2)=B/2-2  #B:brown의 값
    #(n-2)*(m-2)=Y      #Y:yellow의 값
    check_num=divisors_list(yellow) #m-2가 될 수 있는 수
    for i in check_num: #i=m-2
        if yellow//i == (brown//2)-2-i:
            n=(yellow//i)+2
            m=i+2
            break
    answer = [n,m]
    return answer