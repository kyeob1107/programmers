def solution(k, m, score):
    answer = 0
    score.sort(reverse=True) #리스트 내림차순으로 정렬
    for i in range(0,len(score),m): #m개씩 컷트
        if len(score)-i<m: #남은게 m미만이면 중단
            break
        answer+=score[i+m-1]*m #점수 추가하면서 계산
    return answer

'''def solution(k, m, score): #시간이 오래걸려서 수정
    answer = 0
    score.sort(reverse=True) #리스트 내림차순으로 정렬
    for i in range(0,len(score),m): #m개씩 컷트
        if len(score[i:])>=m: #남은게 m개 이상일때만 진행
            answer+=score[i+m-1]*m #점수 추가하면서 계산
    return answer'''