import sys
INF=99999999999
V, E = map(int, input().split())

chart = [[INF for j in range(V+1)] for i in range(V+1)]

for i in range(E):
    start, dest, val = map(int, sys.stdin.readline().split())
    chart[start][dest] = val

for i in range(1, V+1):
    chart[i][i]=0

for i in range(1, V+1):
    for j in range(1, V+1):
        for k in range(1, V+1):
            chart[j][k] = min(chart[j][i] + chart[i][k], chart[j][k])
ans=INF
for i in range(1, V+1):
    for j in range(1, V+1):
        if i !=j:
            ans = min(ans, chart[i][j] + chart[j][i])



print(-1 if ans == INF else ans)