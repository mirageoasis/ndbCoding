from itertools import combinations
from collections import deque

n, m = map(int, input().split())
graph=[[]for i in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)
    graph[a].append(b)
ans_list=[-1, -1, 500000]
for a, b in combinations([i for i in range(1, n+1)], 2):
    que=deque()
    visit=[False for _ in range(0, n+1)]
    que.append([a, 0])
    que.append([b, 0])
    visit[a]=True
    visit[b]=True
    ans=0
    while que:
        pt, time = que.popleft()
        ans+=time*2
        for g in graph[pt]:
            if not visit[g]:
                visit[g]=True
                que.append([g, time+1])
    
    if ans_list[2] > ans:
        ans_list[0]=a
        ans_list[1]=b
        ans_list[2]=ans

print(*ans_list)