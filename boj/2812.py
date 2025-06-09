from collections import deque
n, k = map(int, input().split())
string=list(map(int, list(input())))

# 지렁이 같이 출발
number=""
start_idx=0

if n == 1:
    print("".join(string))
    exit(0)

stack=[]

for s in string:
    while k > 0 and stack and stack[-1] < s:
        stack.pop()
        k-=1
    stack.append(s)
    #print(stack)

#print(stack+string[idx:])

if k > 0:
    stack = stack[:-k]
stack=list(map(str, stack))
print("".join(stack))

#print(string[idx:])
#print(number)