def solution(keymap, targets):
    answer = []
    for string in targets:
        count=0 #글자별로 초기화
        sw1="run" #더 반복문 돌릴 필요 없을 경우는 스킵하기 위해
        for i in range(len(string)):
            min_check=[0 for i in keymap] #횟수기록 초기화
            for j in range(len(keymap)): #버튼종류별 반복문
                if string[i] in keymap[j]:
                    min_check[j]=keymap[j].index(string[i])+1    
                if j+1==len(keymap): #버튼별 전부 확인후 정산적용
                    if max(min_check)>0:
                        count+= min(list(filter(lambda x: x > 0, min_check)))
                    else:
                        count=-1  #전부 다 확인해서 없으면 -1값 저장
                        sw1="stop"
            if sw1 == "stop":
                break
        answer.append(count)
        
    return answer