def solution(sizes):
    #print(sizes[:][:][1]) #이거 왜 2번째 원소인 리스트로 나오냐
    long=0 #가로 세로든 긴 쪽
    short=0 #가로 세로든 짧은 쪽
    for i in sizes:
        if i[0]<i[1]:
            i[0],i[1] = i[1], i[0] #앞쪽으로 긴게 오도록 정렬 #size자체도 수정되는지 테스트
    #print(sizes) #성공적으로 수정됨
        if long<i[0]:
            long=i[0]
        if short<i[1]:
            short=i[1]        
    return long*short