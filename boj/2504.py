string = input()
ans = 0

multi = 1   
stack = []

dic = {
    "(" : 2,
    "[" : 3,
}

rever = {
    ")" : "(",
    "]" : "["
}

for idx ,i in enumerate(string):
    if i == '(' or i == '[':
        # stack 에 추가
        stack.append(i)
        multi *= dic[i]
    elif i == ']' or i == ')':
        if stack and stack[-1] == rever[i]:
            elem = stack.pop()
            multi //= dic[elem]
            if string[idx - 1] == elem:
                ans += (multi * dic[elem])
        else:
            ans = 0
            break

if stack:
    ans = 0

print(ans * multi)