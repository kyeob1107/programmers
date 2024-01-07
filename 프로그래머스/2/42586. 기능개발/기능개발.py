def solution(progresses, speeds):
    answer = []
    if len(progresses)!=len(speeds):
        print("주어진 데이터가 맞지 않습니다")
        return False
    
    complete=[]
    for cal in range(len(progresses)):
        if (100-progresses[cal])%speeds[cal]==0:
            date_require=(100-progresses[cal])//speeds[cal]
        else:
            date_require=1+(100-progresses[cal])//speeds[cal]
        complete.append(date_require)
        
    while len(complete)>0:
        check=complete.pop(0)
        count=1
        while len(complete)>0:
            if check>=complete[0]:
                complete.pop(0)
                count+=1
            else:
                break
        
        answer.append(count)
        count=0
    return answer