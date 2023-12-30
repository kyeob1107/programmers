def solution(s, skip, index):
    trans = list(s) #문자를 변환할 때 저장할 변수 #a~z : 97~122
    skip_list=sorted([ord(i) for i in skip]) #skip에 해당하는 문자 아스키코드
    for i in range(len(trans)):
        move=0
        for j in range(index):
            move+=1

            while (ord(trans[i])+move > ord("z") or ord(trans[i])+move in skip_list):
                if ord(trans[i])+move > ord("z"): #z에서 다시 넘어갈경우 추가계산
                    move-=26
                while ord(trans[i])+move in skip_list:
                    move+=1
                    
        trans[i]=chr(ord(trans[i])+move)
        
    return ''.join(trans)
