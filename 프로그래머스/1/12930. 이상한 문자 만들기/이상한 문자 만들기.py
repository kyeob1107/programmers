def solution(s):
    pre_list=s.split(' ')
    answer = ''
    for i in range(len(pre_list)):
        for j in range(len(pre_list[i])): #띄어쓰기 기준을 나눈 문자 연산
            if j%2==0:
                answer+=pre_list[i][j].upper()
            else:
                answer+=pre_list[i][j].lower()
        answer+=' ' #한 단어가 끝나면 공백추가
    answer=answer[:-1]
    return answer