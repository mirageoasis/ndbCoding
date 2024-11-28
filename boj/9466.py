import time
from collections import deque
T=int(input())

def bfs(start, chart):
    if chart[start] == start:
        return [start]
    ret=[]
    que=deque()
    que.append(start)
    new_visit=[False for i in range(len(chart))]

    flag=False
    while que:
        now_point=que.popleft()
        #print(que)
        #time.sleep(0.5)
        if chart[now_point] == start:
            ret.append(now_point)
            flag=True
            break
        
        if not new_visit[chart[now_point]]:
            ret.append(now_point)
            new_visit[chart[now_point]]=True
            que.append(chart[now_point])
    
    if flag:
        return ret
    else:
        return []

for _ in range(T):
    N=int(input())
    chart=list(map(int, input().split()))
    chart.insert(0, 0)
    visit=[False for i in range(len(chart))]

    for i in range(1, len(chart)):
        if not visit[i]:
            t = bfs(i, chart)
            #print(t)
            for k in t:
                visit[k]=True
        #print(i)
    #print(visit)
    print(visit.count(False) - 1)
