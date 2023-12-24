def solution(s, n):
    trans = list(s) #문자를 변환할 때 저장할 변수 #a~z : 97~122
                #A~Z : 65~90, 공백 : 32 ,공백은 공백으로 남겨두기
    print(trans)
    for i in range(len(trans)):
        if trans[i] == ' ': #사실 바로 조건문 아닐 때만 걸어도 될듯
            continue
        else:                  #\는 줄바꿈표시
            if ord(trans[i])+n > ord("z") \
            or (ord(trans[i])+n>ord("Z") and ord(trans[i])<ord("a")):
                print("확인")
                trans[i]=chr(ord(trans[i])-26)
            trans[i]=chr(ord(trans[i])+n)
    return ''.join(trans)