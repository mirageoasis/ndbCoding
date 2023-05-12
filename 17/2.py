N, M = map(int, input().split())

INF = 1

chart = [[INF for i in range(N+1)] for j in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    chart[a][b] = 0

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            chart[i][j] = min(chart[i][j], chart[i][k] + chart[k][j])

for i in range(1, N+1):
    for j in range(1, N+1):
        if chart[i][j] == INF:
            chart[i][j] = chart[j][i]
        elif chart[j][i] == INF:
            chart[j][i] = chart[i][j]
cnt=0
for i in chart[1:]:
    if i[1:].count(1) == 1:
        cnt+=1

print(cnt)
