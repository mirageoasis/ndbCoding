import sys

n, m = map(int, input().split())
li=[]
graph=[[] for i in range(n+1)]

for i in range(m):
    li.append(list(map(int, sys.stdin.readline().split())))

start, end = map(int, input().split())

li.sort()

for a,b in li:
    graph[a].append(b)
    graph[b].append(a)

visit=[False for i in range(n+1)]
first_visit=set()

from collections import deque

que=deque()
que.append([start, [start]])

while que:
    st, path = que.popleft()
    if st == end:
        first_visit = set(path)
        break
    for i in graph[st]:
        if not visit[i]:
            visit[i]=True
            c=path[:]
            c.append(i)
            que.append([i, c])

visit=[False for i in range(n+1)]

for i in first_visit:
    if i not in [start, end]:
        visit[i]=True

que=deque()
que.append([end, [end]])
second_visit=set()

while que:
    st, path = que.popleft()
    if st == start:
        second_visit = set(path)
        break
    for i in graph[st]:
        if not visit[i]:
            visit[i]=True
            c=path[:]
            c.append(i)
            que.append([i, c])

#print(first_visit, second_visit)
print(len(first_visit) + len(second_visit) - 2)
