import sys
from collections import deque

n=int(input())

graph=[[] for i in range(n+1)]

for i in range(n-1):
    a, b =map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)


visit=[False for i in range(n+1)]
color=[False for i in range(n+1)]
child_list=[]
for i in range(1, n+1):
    if len(graph[i]) == 1:
        child_list.append(i)
        visit[i]=True

que=deque(child_list)


while que:
    point = que.popleft()

    for i in graph[point]:
        if not visit[i]:
            que.append(i)
            visit[i]=True
        if not color[point] and len(graph[i]) != 1:
            color[i]=True

#print(color)
print(color.count(True))