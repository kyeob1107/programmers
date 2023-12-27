def solution(lottos, win_nums):
    answer = [6,6] #초기값으로 6등 낙찰 정의
    lottos.sort()
    win_nums.sort()
    count=0
    for i in win_nums:
        if i in lottos:
            count+=1
    if count>1 : #최저등수 기록
        answer[1]=7-count
    #지어진 부분이 다 맞다고 가정하고 계산시
    for i in lottos:
        if i == 0 :
            count+=1
        else: #정렬해뒀으니 0이 아니면 그뒤로 더이상 0이 없을 것이기 때문에
            break
    if count>1 : #최고등수 기록
        answer[0]=7-count
    
    return answer