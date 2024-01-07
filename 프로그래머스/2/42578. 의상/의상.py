def solution(clothes):
    answer = 1
    type_dict={}
    for i in clothes:
        if i[1] in type_dict:
            type_dict[i[1]]+=1
        else:
            type_dict[i[1]]=1
    for j in list(type_dict.values()):
        answer*=(j+1)
    return answer-1