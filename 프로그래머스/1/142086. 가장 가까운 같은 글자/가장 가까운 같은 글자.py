def solution(s):
    answer = []
    #print(s[:0])
    for i in range(len(s)):
        if s[i] not in s[:i]:
            answer.append(-1)
        else:
            for j in range(len(s[:i])):
                if s[i]==s[:i][::-1][j]:
                    answer.append(j+1)
                    break #가장 가까운 같은 글자 찾았으면 반복하면서 확인그만
                          #추가 확인하면 여러번 차이값을 답에 추가하게 됨
    return answer