from collections import deque
first=input()
second=input()
que=deque()
que.append(second)
flag=0
while que:
    s = que.popleft()
    #print(s)
    if s == first:
        flag=1
        break
    if len(s) == 1:
        continue

    if s[-1] == "A":
        que.append(s[:-1])
    
    if s[0] == "B":
        t=list(reversed(list(s[1:])))
        que.append(''.join(t))

    
print(flag)