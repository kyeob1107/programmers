def solution(t, p):
    #len(p) 짧은 문자열의 갯수 필요
    #if "12"<"52": #숫자로된 문자열끼리도 크기 비교해주는지 확인
    #    print("yes")
    answer = 0
    num_list=[t[i:i+len(p)] for i in range(len(t)) if len(t[i:])>=len(p)]
    for j in num_list:
        if j<=p:
            answer+=1
    return answer