# 탐색할 행성의 개수
# 발사되는 행성의 위치
# 이동을 하는데 걸리는 시간
# 모든 곳 탐사 최소시간
# mst

import sys

N, start = map(int, input().split())

chart = []
graph = []
parent = [i for i in range(N)]

for i in range(N):
    chart.append(list(map(int, sys.stdin.readline().split())))

for i in range(N):
    for j in range(N):
        if i != j:
            graph.append((i, j, chart[i][j]))


for i in range(N):
    for j in range(N):
        for k in range(N):
            chart[j][k] = min(chart[j][k], chart[j][i] + chart[i][k])

ans=1000000000000

def back(start, depth, N, now_ans, chart, visit):
    global ans
    #print(visit)
    if N - 1 == depth:
        ans=min(ans, now_ans)
        return
    
    for i in range(N):
        if not visit[i]:
            visit[i] = True
            back(i, depth+1, N, now_ans+chart[start][i], chart, visit)
            visit[i] = False


visit = [False for i in range(N)]

visit[start] = True
back(start, 0, N, 0, chart, visit)
visit[start] = False

print(ans)