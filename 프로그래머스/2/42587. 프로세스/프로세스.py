def solution(priorities, location):
    answer = 0
    index=list(range(len(priorities))) #큐라고 생각(이름을 인덱스로)
    while len(index)>0:
        process=index.pop(0) #큐의 첫번째 프로세스
        pro_prior=priorities.pop(0) #큐의 첫번째 프로세스의 우선순위
        if len(priorities)!=0:
            if pro_prior>=max(priorities): #우선순위 가장 높거나 같다면 실행
                answer+=1
                if process == location :
                    return answer
            else:
                index.append(process)
                priorities.append(pro_prior)
        else: #마지막이라 더이상 비교할 대상 없을경우 그냥 마저 실행하고 +1
            return answer+1
                
    print("다 체크했는데 뭔가 오류가 있음!")
    return answer