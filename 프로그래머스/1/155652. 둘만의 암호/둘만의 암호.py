def solution(s, skip, index):
    answer=''
    able_list=[chr(ord('a')+i) for i in range(ord('z')-ord('a')+1)] #가능한 목록
    for i in skip: #스킵에 있는 얘들 제거
        able_list.remove(i)
    for j in range(len(s)):
        answer+=able_list[(able_list.index(s[j])+index)%len(able_list)]
        
    return answer
