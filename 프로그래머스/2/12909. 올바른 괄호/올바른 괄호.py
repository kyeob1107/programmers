def solution(s):
    answer = True
    stack=[]
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    if len(stack)>0: #모든 문자에 대해 확인했는데 스택이 남아있으면 X
        return False
    return True