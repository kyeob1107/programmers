def solution(want, number, discount):
    answer = 0
    want_dict={key:value for key,value in zip(want,number)}
    #10일간 회원유지되므로 이정도만 반복체크
    for day_index in range(len(discount)-9): 
        check_dict={}
        switch='Y'
        for update in discount[day_index:day_index+10]:
            if update in check_dict:
                check_dict[update]+=1
            else:
                check_dict[update]=1
        for check in want_dict:
            if check not in check_dict:
                switch='N'
                break
            else:
                if check_dict[check]<want_dict[check]:
                    switch='N'
                    break
        if switch=='Y':
            answer+=1
    
    return answer