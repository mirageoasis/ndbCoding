#9시 21분에 시작
import sys
from collections import deque

N, M = map(int, input().split())
chart=[[] for i in range(N+1)]

def bfs(start):
    global N, M
    visit=[False for i in range(N+1)]
    visit[0]=True
    visit[start]=True
    que=deque()
    que.append((start, 0))
    ret=0
    while que:
        pt, time = que.popleft()
        ret+=time

        for i in chart[pt]:
            if not visit[i]:
                visit[i]=True
                que.append((i, time+1))
    return ret

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    chart[a].append(b)
    chart[b].append(a)

maxi=999999999
idx=0
for i in range(1, N+1):
    ret=bfs(i)
    if maxi > ret:
        idx=i
        maxi=ret

print(idx)