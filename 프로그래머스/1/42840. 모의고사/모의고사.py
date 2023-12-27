def solution(answers):
    #1번 12345  5개마다
    #2번 21232425  8개마다
    #3번 3311224455 10개마다
    a1=[1,2,3,4,5] #1번 수험자가 내는 순서
    a2=[2,1,2,3,2,4,2,5] #2번 ""
    a3=[3,3,1,1,2,2,4,4,5,5] #3번 ""
    a1_c=0 #1번 수험자가 정답 맞춘 수
    a2_c=0 #2번 ""
    a3_c=0 #3번 ""
    answer = []
    for i in range(len(answers)):
        if answers[i]==a1[i%len(a1)]:
            a1_c+=1
        if answers[i]==a2[i%len(a2)]:
            a2_c+=1
        if answers[i]==a3[i%len(a3)]:
            a3_c+=1
        
    max_c=max(a1_c,a2_c,a3_c) #최대 정답 수
    if a1_c==max_c:
        answer.append(1)
    if a2_c==max_c:
        answer.append(2)
    if a3_c==max_c:
        answer.append(3)
    return answer