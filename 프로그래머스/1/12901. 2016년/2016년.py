def solution(a, b):
    month_inf=[31,29,31,30,31,30,31,31,30,31,30,31] #1~12월 일수
    week_inf=["FRI","SAT","SUN","MON","TUE","WED","THU"]
            #하루 차이나면 토요일이 되도록 설정하여 리스트 생성
    return week_inf[(sum(month_inf[:a-1])+(b-1))%7]

#아래 부분 보기 편하게 하면
    '''answer = (sum(month_inf[:a-1])+(b-1))%7
      #(차이나는 달만큼 일수 계산+ 일자별끼리 계산)를 7로 나눴을때 나머지
    return week_inf[answer]'''
