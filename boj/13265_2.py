import sys
from collections import deque

t=int(input())


graph=[]
visit=[]
color=[]
vertex=0
edge=0
def bfs(start_point):
    global vertex, edge, graph, color, visit
    que=deque()
    que.append(start_point)
    while que:
        now_point=que.popleft()

        for i in graph[now_point]:
            if not visit[i]:
                #print(i, color[now_point], color[now_point] ^ 1)
                visit[i]=True
                color[i]= color[now_point] ^ 1
                que.append(i)
            else:
                if color[i] == color[now_point]:
                    return False

    return True

for _ in range(t):
    vertex, edge = map(int, input().split())
    graph=[[]for i in range(vertex+1)]
    visit=[False for i in range(vertex+1)]
    color=[-1 for i in range(vertex+1)]

    for i in range(edge):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    flag=True
    for i in range(1, vertex+1):
        if not visit[i]:
            visit[i]=True
            color[i]=0
            flag &= bfs(i)
        if not flag:
            break
    #print(color)
    if flag:
        print("possible")
    else:
        print("impossible")

