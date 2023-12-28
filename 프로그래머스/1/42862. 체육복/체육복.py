def solution(n, lost, reserve):
    backup=0
    #여분있는 학생이 도난됬을 경우 적용하여 업데이트할 임시 저장리스트
    lost_update=[]
    for i in lost:
        if i not in reserve:
            lost_update.append(i)
        else: #reserve도 거기 맞게 업데이트
            reserve.remove(i)
    lost=lost_update
    lost.sort()
    for i in range(len(lost)):
        if lost[i]-1 in reserve or lost[i]+1 in reserve:
            #lost.pop(i) #이것때문에 반복문에 문제가 생겨서 따로 카운트함
            #앞뒤로 둘다있다면 앞쪽부터 확인하고 있으니 앞쪽것을 사용
            if lost[i]-1 in reserve and lost[i]+1 in reserve:
                reserve.remove(lost[i]-1)
                backup+=1
            else:
                if lost[i]-1 in reserve:
                    reserve.remove(lost[i]-1)
                    backup+=1
                elif lost[i]+1 in reserve:
                    reserve.remove(lost[i]+1)
                    backup+=1
    return n-len(lost)+backup