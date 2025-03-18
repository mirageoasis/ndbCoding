import time
from collections import deque
T=int(input())
chart=[]
def bfs(start):
    global chart, visit
    if chart[start] == start:
        return 1
    ret=[]
    que=deque()
    que.append((start, 1))
    order_dict=dict()
    order_dict[start]=1
    
    while que:
        now_point, idx=que.popleft()
        #print(que)
        #time.sleep(0.5)
        next_pt=chart[now_point]
        if next_pt in order_dict:
            #print(idx, next_pt, order_dict[next_pt])
            return idx - order_dict[next_pt] + 1
        
        if not visit[next_pt]:
            visit[next_pt]=True
            order_dict[next_pt]=idx+1
            que.append((next_pt, idx+1))
    
    return 0


for _ in range(T):
    N=int(input())
    chart=list(map(int, input().split()))
    chart.insert(0, 0)
    visit=[False for i in range(len(chart))]
    ans=0
    for i in range(1, len(chart)):
        if not visit[i]:
            #print(visit[i], i)
            t = bfs(i)
            visit[i]=True
            ans+=t
            #print(visit, t)
    #print(visit)
    print(len(chart)-ans-1)
