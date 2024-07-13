import sys
input = sys.stdin.readline
data = input().strip()
stack = []
not_correct = False
for i, s in enumerate(data):
    if s == '(':
        stack.append(s) # 2
    
    elif s == '[':
        stack.append(s) # 3
    
    else:
        check_stack = [d for d in stack if type(d) == str]
        if not check_stack:
            not_correct = True
            break
        elif (check_stack[-1] == '[' and s == ')'):
            not_correct = True
            break
        elif (check_stack[-1] =='(' and s == ']'):
            not_correct = True
            break
        
        elif (stack[-1] == '(' and s == ')'):
            stack.pop()
            stack.append(2)
        
        elif (stack[-1] == '[' and s == ']'):
            stack.pop()
            stack.append(3)
        
        elif (type(stack[-1]) == int):
            val = stack.pop()
            while stack and type(stack[-1]) == int:
                val += stack.pop()
            if stack and s in [')', ']']: # 비었으면 index 에러 날 수 있어서
                if stack[-1] == '(':
                    stack.pop()
                    stack.append(2 * val)
                elif stack[-1] == '[':
                    stack.pop()
                    stack.append(3 * val)
        
if not_correct or any(isinstance(d, str) for d in stack):
    print(0)
else:
    print(sum(stack))