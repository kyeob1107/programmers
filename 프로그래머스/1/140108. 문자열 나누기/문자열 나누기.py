def solution(s):
    answer = 0
    same_str=''
    same_num=0
    other_num=0
    for i in range(len(s)):
        if same_num==0: #같은 문자로 체크할 문자 저장
            same_str=s[i]
            same_num+=1
        elif same_str==s[i]:
            same_num+=1
        else: #세고 있는 글자가 있고 다른문자가 나올경우 아마 마지막꼬다리가 문제될수도
            other_num+=1
            if same_num==other_num: #세고있던 글자와 다른글자 수가 같아질 경우
                answer+=1 #문자열을 한번 나눠준다(실제로는 안하고 횟수만 체크)
                same_num=0 #그리고 다시 세던횟수는 초기화
                other_num=0
        if i==len(s)-1 and same_num!=other_num: #마지막 것인지 체크
            answer+=1
    return answer

#시각화 해서 체크 편하기용
'''def solution(s):
    answer = 0
    same_str=''
    split_str='' #시각적 체크용 나중에 삭제
    same_num=0
    other_num=0
    for i in range(len(s)):
        if same_num==0: #같은 문자로 체크할 문자 저장
            same_str=s[i]
            same_num+=1
            split_str=''
        elif same_str==s[i]:
            same_num+=1
        else: #세고 있는 글자가 있고 다른문자가 나올경우 아마 마지막꼬다리가 문제될수도
            other_num+=1
            if same_num==other_num: #세고있던 글자와 다른글자 수가 같아질 경우
                answer+=1 #문자열을 한번 나눠준다(실제로는 안하고 횟수만 체크)
                same_num=0 #그리고 다시 세던횟수는 초기화
                other_num=0
        if i==len(s)-1 and same_num!=other_num: #마지막 것인지 체크
            answer+=1
        split_str+=s[i]
        print(answer,split_str,same_str,same_num,other_num)
    return answer'''