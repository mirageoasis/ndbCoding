# 9시 12분

# 친구와 친구
import sys
from collections import deque

N=int(input())
M=int(input())

chart=[[] for i in range(N+1)]
visit=[False for i in range(N+1)]

def bfs():
    que=deque()
    que.append((1, 1))
    visit[1]=True

    while que:
        pt, time = que.popleft()

        if time == 3:
            break
        for i in chart[pt]:
            if not visit[i]:
                visit[i]=True
                que.append((i, time+1))

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    chart[a].append(b)
    chart[b].append(a)

bfs()

print(visit.count(True) - 1)