from collections import deque
import time

t=int(input())
LIM=3000001
is_prime=[True for i in range(LIM)]

is_prime[0]=False
is_prime[1]=False
for i in range(2, LIM):
    if is_prime[i]:
        for j in range(i*2, LIM, i):
            is_prime[j]=False

def bfs(start):
    global visit, number, left, right, LIM
    que=deque()
    que.append((start, 0))

    while que:
        now, times=que.popleft()
        #print(now)
        if left<=now<=right and is_prime[now]:
            return times

        # 들어와 있으면 소수 검사

        # 절반
        if now//3 != 0 and not visit[now//3]:
            visit[now//3]=True
            que.append((now//3, times+1))
        # 3/1
        if now//2 != 0 and not visit[now//2]:
            visit[now//2]=True
            que.append((now//2, times+1))

        # 덧셈 뺄셈
        if now+1 < LIM and not visit[now+1]:
            visit[now+1]=True
            que.append((now+1, times+1))
        
        if now-1 > 0 and not visit[now-1]:
            visit[now-1]=True
            que.append((now-1, times+1))

    
    return -1

for _ in range(t):
    number, left, right = map(int, input().split())
    
    visit = [False for i in range(LIM)]
    visit[number]=True
    print(bfs(number))