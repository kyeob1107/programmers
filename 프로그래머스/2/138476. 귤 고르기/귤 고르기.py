def solution(k, tangerine):
    num_check={} #크기별 몇개있는지 기록
    box=[] #가상의 진짜 박스
    answer = 0
    for size in tangerine: #크기별로 몇 개씩 있는지 저장
        if size in num_check:
            num_check[size] += 1
        else:
            num_check[size] = 1
            
    std=max(num_check.values()) #standard 넣을 귤 갯수 기준
    while len(box)<k:
        for key in num_check:
            if num_check[key]==std:
                box.extend([i for i in range(num_check[key])])
                answer+=1
                if len(box) >=k:
                    break
        std-=1
        if std<=0: #혹시나 더이상 넣을 것이 없으면 중단
            print("더 넣을 것이 없는데요")
            break
    
    return answer