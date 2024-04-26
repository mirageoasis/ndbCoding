import sys
from collections import deque

T=int(input())

def bfs(start, graph, visit):
    que = deque()
    que.append(start)

    while que:
        po = que.popleft()
        for i in graph[po]:
            if not visit[i]:
                visit[i] = visit[po] * -1
                que.append(i)
            else:
                if visit[i] == visit[po]:
                    return False
    return True

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    
    visit = [0 for i in range(N+1)]
    graph = [[] for i in range(N+1)]

    for i in range(M):
        first, second = map(int, sys.stdin.readline().split())
        graph[first].append(second)
        graph[second].append(first)
    cnt=0
    for i in range(1, N+1):
        if not visit[i]:
            visit[i]=1
            if(not bfs(i, graph, visit)):
                cnt+=1
    if cnt > 0:
        print("impossible")
    else:
        #print(cnt)
        print("possible")

