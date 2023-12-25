def solution(array, commands):
    answer = []
    cut=[]
    for i in commands:
        cut=array[i[0]-1:i[1]]  #앞에는 0부터 시작하니 -1해줘서 맞추고 
        cut.sort()              #뒤에는 해당전까지니 굳이 보정해줄 필요 없음
        answer.append(cut[i[2]-1])
    return answer