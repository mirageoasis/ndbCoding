import sys

input=sys.stdin.readline

n=int(input())
first, second=map(int, input().split())
m=int(input())

graph=[[]for i in range(n+1)]

for i in range(m):
    a, b=map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(start, end):
    global n, graph
    from collections import deque
    que=deque()
    visit=[False for i in range(n+1)]
    que.append((start, 0))
    visit[start]=True
    while que:
        now, dist = que.popleft()
        if now == end:
            return dist
        for i in graph[now]:
            if not visit[i]:
                que.append((i, dist+1))
                visit[i]=True
    
    return -1

print(bfs(first, second))
