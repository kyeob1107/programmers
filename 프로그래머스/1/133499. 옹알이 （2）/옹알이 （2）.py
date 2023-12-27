def solution(babbling):
    answer = 0
    can=["aya", "ye", "woo", "ma" ]
    for i in babbling:
        for c in can:
            if c*2 not in i: #연속으로 쓰이는 부분이 있으면 발음불가이므로
                i=i.replace(c,' ')#아닌경우에대해서만 계산
        if i.isspace():
            answer+=1
    return answer

#해당하는 부분 공백으로 만들다보면 순서대로 다 해당하게 되었다면
#공백만 남을 것이지만, 해당하는 단어로 규칙에 맞게 지울수 없다면 글자가 남게 되므로
#공백인지 판별하는 메소드를 통해 판별 가능할 것이다