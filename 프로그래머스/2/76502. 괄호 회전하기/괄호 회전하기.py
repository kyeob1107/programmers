def solution(s):
    def is_valid(string):
        stack = []
        for char in string:
            if char in ['[', '(', '{']:
                stack.append(char)
            else:
                if not stack:
                    return False
                if char == ']' and stack[-1] == '[':
                    stack.pop()
                elif char == ')' and stack[-1] == '(':
                    stack.pop()
                elif char == '}' and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
        return not stack

    if len(s) % 2 != 0:
        return 0

    count = 0
    for i in range(len(s)):
        rotated = s[i:] + s[:i]
        if is_valid(rotated):
            count += 1

    return count

def msj(s):
    answer = 0
    len_s = len(s)
    s += s
    
    for i in range(len_s):
        check = ""
        for s_val in s[i:i+len_s]:
            if s_val == '(':
                check += '1'
            elif s_val == '{':
                check += '2'
            elif s_val == '[':
                check += '3'
            else:
                if check == "":
                    check = "0"
                    break
                elif check[-1] == '1' and s_val == ')':
                    check = check[:-1]
                elif check[-1] == '2' and s_val == '}':
                    check = check[:-1]
                elif check[-1] == '3' and s_val == ']':
                    check = check[:-1]
        if check == "":
            answer += 1
    
    return answer

# 테스트
print(solution("({[)}]"))  # 0
print(msj("({[)}]"))  # 0
