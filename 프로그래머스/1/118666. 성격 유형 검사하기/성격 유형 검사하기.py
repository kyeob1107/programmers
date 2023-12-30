def solution(survey, choices):
    answer = ''
    score={'R':0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0}
    
    for i in range(len(survey)):
        if choices[i] in [1,2,3]: #1,2,3으로 응답시 앞에 문자에 점수
            score[survey[i][0]] += 4-choices[i]
        elif choices[i] in [5,6,7]: #5,6,7으로 응답시 뒤에 문자에 점수
            score[survey[i][1]] += choices[i]-4
    #문자별 점수 비교 및 결정
    #RT
    if score['R'] >= score['T'] :
        answer+='R'
    else:
        answer+='T'
    #CF
    if score['C'] >= score['F'] :
        answer+='C'
    else:
        answer+='F'
    #JM
    if score['J'] >= score['M'] :
        answer+='J'
    else:
        answer+='M'
    #AN
    if score['A'] >= score['N'] :
        answer+='A'
    else:
        answer+='N'   
    return answer

#항상 대문자라는 제한조건이 안 보이던데 안 넣어도 될련지