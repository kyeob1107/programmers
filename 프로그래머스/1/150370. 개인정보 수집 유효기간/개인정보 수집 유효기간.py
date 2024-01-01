def solution(today, terms, privacies):
    answer = []
    t_y,t_m,t_d=today.split('.') #여기서 바로 int로 바꾸는 방법은 없나?
    today_value=int(t_y)*12*28+int(t_m)*28+int(t_d)
    term_dict={i.split()[0]:int(i.split()[1])*28 for i in terms}
    
    for i in range(len(privacies)) :
        y,m,d=privacies[i].split('.') #년,월,일 약관종류 로 저장
        d,t=d.split() #일, 약관종류로 분리
        date_value=int(y)*12*28+int(m)*28+int(d)
        if today_value-date_value >= term_dict[t] :
            answer.append(i+1)
        
    return answer

#좀더 성능 개선 가능한지 테스트 해볼 경우 많을듯
#지금은 그냥 for문 안에서 매번 나눠서 사용했는데
#privacies에서 그냥 바로 띄어쓰기 .으로 바꿔서 한번에 해도 괜찮을지도