# 거리가 n 이내라면 그냥 graph에 포함

n, r, d, x, y = map(int, input().split())

li=[]
graph=[[] for i in range(n)]

for i in range(n):
    li.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        x_i, y_i = li[i]
        x_j, y_j = li[j]
        if (x_i - x_j) ** 2 + (y_i - y_j) ** 2 <= r ** 2:
            graph[i].append(j)

# li는 i에 있는 좌표

from collections import deque
que=deque()
visit=[False for i in range(n)]

for i in range(n):
    x_i, y_i = li[i]    
    if (x_i - x) ** 2 + (y_i - y) ** 2 <= r ** 2:
        que.append((i, 1))
        visit[i]=True
#print()
ans=0
while que:
    idx, div = que.popleft()
    ans+= d/div
    #print(idx, d/div)
    for i in graph[idx]:
        if not visit[i]:
            visit[i]=True
            que.append((i, div*2))

print(ans)