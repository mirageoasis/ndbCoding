N = int(input())
M = int(input())

INF = 10000000000

dis = [[INF for i in range(N+1)] for j in range(N+1)]

for _ in range(M):
    start, dest, d = map(int, input().split())
    dis[start][dest] = min(d, dis[start][dest])

for i in range(1, N+1):
    dis[i][i] = 0

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            dis[i][j] = min(dis[i][k] + dis[k][j], dis[i][j])

#print(li)

for i in range(1, N+1):
    for j in range(1, N+1):
        if dis[i][j] == INF:
            print(0, end= ' ')
        else:
            print(dis[i][j], end=' ')
    print()