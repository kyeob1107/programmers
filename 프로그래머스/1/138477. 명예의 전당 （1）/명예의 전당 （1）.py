def solution(k, score):
    answer = []
    for i in range(len(score)): #for i+1 in~이렇게하면 어떻게되는지 까먹음
                                #테스트필요
        rnk_scr=sorted(score[:i+1],reverse=True)
        answer.append(min(rnk_scr[:k]))
        
    return answer