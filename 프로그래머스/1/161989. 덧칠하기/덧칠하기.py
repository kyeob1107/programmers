def solution(n, m, section):
    answer = 0
    wall= [1 for i in range(n+m)] #안 칠해진 부분을 0으로 표기
    for i in section:  #칠해야 하는 빈 곳 적용 i=구역번호
        wall[i-1]=0 #2번 벽의 인덱스 주소의 경우 1이므로 번호-1
         #존재하지 않는 리스트 계산을 위한 가상의 벽을 룰러 길이만큼 벽에 추가
    for j in range(n):  #벽 칠하기 작업 여기선 인덱스와 번호 맞춰주기
        if wall[j]==0:  #j=인덱스
            for k in range(j,j+m): #m개를 같이 칠할 수 있으므로
                wall[k]+=1 
            answer+=1    
    return answer