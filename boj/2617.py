# 30분
from collections import deque
N, M = map(int, input().split())

high_graph=[[] for i in range(N+1)]
low_graph=[[] for i in range(N+1)]


for i in range(M):
    a, b = map(int, input().split())
    high_graph[a].append(b)
    low_graph[b].append(a)

def bfs(grahp, start):
    global N
    visit=[False for i in range(N+1)]
    visit[start] = True
    que=deque()
    que.append(start)
    
    while que:
        point = que.popleft()

        for i in grahp[point]:
            if not visit[i]:
                visit[i]=True
                que.append(i)
    #print(start, visit[1:])
    visit[start]=False
    return visit.count(True)
ans=0

for i in range(1, N+1):
    if bfs(low_graph, i) >= N//2 + 1 or bfs(high_graph, i) >= N//2 + 1:
        #print(i)
        ans+=1

print(ans)