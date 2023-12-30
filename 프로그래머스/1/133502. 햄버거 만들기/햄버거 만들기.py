def solution(ingredient):
    answer = 0
    now=[] #현재 쌓여있는 재료 리스트
    order=[1,2,3,1] #햄버거 쌓을 수 있는 재료순
    order_len=len(order)
    for ing in ingredient:
        now.append(ing)
        if len(now)>=order_len:
            if now[-order_len:]==order:
                answer+=1
                del now[-order_len:]
    return answer

'''def solution(ingredient):
    answer = 0
    s_ing=''#.join(str(i) for i in ingredient) #리스트를 문자열로 변환
    #원래 알던 대로면 [str(i) for i in ingredient]이지만 생략가능한듯
    order='1231'#햄버거 쌓을 수 있는 재료순
    for ing in ingredient:
        s_ing+=str(ing)
        if len(s_ing)>=len(order):
            if s_ing.count(order)>0:
                answer+=1
                s_ing=s_ing.replace(order,'')
    return answer'''