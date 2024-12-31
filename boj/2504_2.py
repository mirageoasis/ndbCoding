chart=list(input())

stack=[]
ans=0
flag=True
for i in chart:
    if not flag:
        break
    
    if i == '[':
        stack.append(i)
    elif i == '(':
        stack.append(i)
    elif i == ']':
        temp_num=0
        find_flag=False
        if not stack:
            flag=False
            break
        while stack:
            out = stack.pop()
            if out == '[':
                if temp_num == 0:
                    stack.append(3)
                    find_flag=True
                    break
                else:
                    stack.append(3 * temp_num)
                    find_flag=True
                    break
            elif out == '(' or out == ']':
                flag=False
                break
            # 숫자
            else:
                temp_num+=out
        if not find_flag:
            flag=False
    elif i == ')':
        temp_num=0
        find_flag=False
        if not stack:
            flag=False
            break
        
        while stack:
            out = stack.pop()
            if out == '(':
                if temp_num == 0:
                    stack.append(2)
                    find_flag=True
                    break
                else:
                    stack.append(2 * temp_num)
                    find_flag=True
                    break
            elif out == '[' or out == ')':
                flag=False
                break
            # 숫자
            else:
                temp_num+=out
        
        if not find_flag:
            flag=False
    #print(stack)

if not flag:
    print(0)
elif '[' in stack or ']' in stack or '(' in stack or ')' in stack:
    print(0)
else:
    print(sum(stack))