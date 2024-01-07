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

def solution(s):
    if len(s) % 2 != 0:
        return 0

    count = 0
    for i in range(len(s)):
        rotated = s[i:] + s[:i]
        if is_valid(rotated):
            count += 1

    return count

#매우 오래걸려서 chatGPT를 통해 수정된 내용 이용 자세한 건 노션24.01.08참고
