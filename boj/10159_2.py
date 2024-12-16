n=int(input())
m=int(input())

INF=999999

dist=[[INF for i in range(n+1)] for j in range(n+1)]

for i in range(m):
    start, end = map(int, input().split())
    dist[start][end]=0

for k in range(n+1):
    for i in range(n+1):
        for j in range(n+1):
            dist[i][j]=min(dist[i][j], dist[i][k] + dist[k][j])

for i in range(1, n+1):
    dist[i][i]=0
    ans=0
    for j in range(1, n+1):
        if dist[i][j]==INF and dist[j][i]==INF:
            ans+=1
    
    print(ans)

# bfs 도 가능하나 플로이드 와샬이 더 간단해서 풀기 쉬움