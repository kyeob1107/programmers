def solution(arr):
    answer = []
    # 순서대로 배열에 대해 반복 for
    # 같은 숫자라면 패스하고 삭제 다른 숫자면 answer에 추가
    for num in arr:
        if len(answer) == 0: #처음엔 넣고 시작
            answer.append(num)
        elif answer[-1] == num: # 같은 숫자라면
            continue
        else:
            answer.append(num)
            
    
    return answer