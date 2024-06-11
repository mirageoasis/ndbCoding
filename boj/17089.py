#45
from sys import stdin

N, M = map(int, input().split())
temp=[]
chart=[[] for i in range(N+1)]

for i in range(M):
    temp.append(list(map(int,stdin.readline().split())))

for a, b in temp:
    chart[a].append(b)
    chart[b].append(a)

# navie 하게 하면
# 4000 C 3
# 4000 * 4000 * 4000 = 64000000000/6
INF=400000
ans=INF
# start, now, sum, times
from collections import deque
for i in range(1, N+1):
    que=deque()
    que.append((i, 0, 0))
    while que:
        now, s, times = que.pop()
        if times > 3:
            continue
            
        if times == 3:
            if i == now:
                ans=min(s, ans)

        for c in chart[now]:
            if times !=2 and c == i:
                continue
            if c < i:
                continue
            #print(s+len(chart[c])-2)
            que.append((c, s+len(chart[c])-2, times+1))

if ans == INF:
    print(-1)
else:
    #print(len(chart[1]), len(chart[3999]), len(chart[4000]))
    print(ans)

