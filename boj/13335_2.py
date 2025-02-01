from collections import deque
n, m, k = map(int, input().split())
li=list(map(int, input().split()))

b_que=deque()
que=deque(li)
for i in range(m):
    b_que.append(0)

ans=0
s=0

while True:
    front=b_que[0]
    #print(b_que)
    #print(que)
    #print()
    if que:
        if s-front+que[0] <= k:
            now=que.popleft()
            b_que.append(now)
            s+=now
        else:
            b_que.append(0)
        s-=front
    else:
        for i in range(m-1, -1, -1):
            if b_que[i]:
                ans+=(i+1)
                break
        break
    b_que.popleft()

    ans+=1

print(ans)