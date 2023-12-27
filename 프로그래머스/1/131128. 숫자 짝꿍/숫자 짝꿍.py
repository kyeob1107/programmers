def solution(X, Y):
    answer=''
    x_dict={'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
    y_dict={'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
    for i in range(10):
        x_dict[str(i)]=X.count(str(i))
        y_dict[str(i)]=Y.count(str(i))
    #print(x_dict)
    #print(y_dict)
    for i in range(9,-1,-1):
        answer+=str(i)*min(x_dict[str(i)],y_dict[str(i)])
        
    if answer =='':
        return "-1"
    
    if answer[0]=="0" and len(answer)>1:
        answer="0"        
    return answer

#리스트 만들어서 정렬 후 리스트가 빠를까 추가할 때 비교해서 넣는게 빠를까