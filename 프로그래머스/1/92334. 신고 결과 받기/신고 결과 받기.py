def solution(id_list, report, k):
    answer = [0 for i in id_list]
    id_index={id:index for id,index in zip(id_list,range(len(id_list)))}
    report_subject={id:[] for id in id_list} #신고한 대상 저장
    report_count={id:0 for id in id_list} #신고카운트하는 딕셔너리
    suspension=[] #정지명단
    for contents in report:
        reporter,subject=contents.split()
        if subject not in report_subject[reporter]:
            report_subject[reporter].append(subject)
            report_count[subject]+=1
                
    for sub in report_count: #딕셔너리는 for문으로 돌릴 때 인덱스으로는 못하나?
        if report_count[sub] >=k:
            suspension.append(sub)
            
    for check in suspension:
        for key in report_subject:
            if check in report_subject[key]:
                answer[id_index[key]]+=1
                      
    return answer

#신고한게 없는 사람, 신고된적이 없는 사람 적을 필요가 있나?
#일단 초기값으로 모든 인원대해서하고 진행해봄