INF=100001
visit=[False for i in range(INF)]
n, m = map(int, input().split())

visit[n]=True

from heapq import heappush, heappop
que=[]
heappush(que, (0, n))
while True:
    times, now = heappop(que)
    visit[now]=True
    if now == m:
        print(times)
        break
    f=now-1
    s=now+1
    t=now*2

    if 0<=f<INF and not visit[f]:
        heappush(que, (times+1, f))
    if 0<=s<INF and not visit[s]:
        heappush(que, (times+1, s))
    if 0<=t<INF and not visit[t]:
        heappush(que, (times, t))