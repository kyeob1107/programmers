def solution(num):
    answer = 0
    if num == 1:
        return 0
    for i in range(500):
        if num%2==0:
            num=num//2
        else:
            num=num*3 +1
        answer+=1
        if num == 1:
            print(answer)
            return answer
    print(answer)
    return -1

#뭔가 수학적으로 파악해서 깔끔하고 빠르게 끝낼 수 있을 것 같은데
#당장 떠오르는게 없어서 일단 단순무식하게 해결하겠음