n, m = map(int, input().split())
li=[]

from collections import deque
que=deque()


for i in range(n):
    que.append(list(map(int, input().split())))
ans=0
buffer=[]
while que:

    p, w = que.popleft()
    flag=False
    for k, v in que:
        if k > p:
            flag=True
            break
    
    if flag:
        ans+=w
        que.append([p, w])

        continue
    
    if buffer and buffer[-1][1] < w and buffer[-1][0] == p:
        other_buffer=[]

        while buffer and buffer[-1][1] < w and buffer[-1][0] == p:

            n_p, n_w = buffer.pop()
            ans+=n_w

            other_buffer.append([n_p, n_w])
        ans+=w

        buffer.append([p, w])
        while other_buffer:
            n_p, n_w = other_buffer.pop()
            ans+=n_w
            buffer.append([n_p, n_w])
    else:
        buffer.append([p, w])
        ans+=w
# 1 /4 1 2 1 /8 1 2 1 /12
print(ans)