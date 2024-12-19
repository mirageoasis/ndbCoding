from collections import deque

n=int(input())
li=list(map(int, input().split()))
start=int(input())-1

visit=[False for i in range(n)]

que=deque()
que.append(start)
visit[start]=True
while que:
    now = que.popleft()
    new_list=[now-li[now], now+li[now]]
    for i in new_list:
        if 0<=i<n and not visit[i]:
            visit[i]=True
            que.append(i)

print(visit.count(True))