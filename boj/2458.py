import sys
input=sys.stdin.readline
n, m = map(int, input().split())

# 0 제외
INF=9999999999
up_chart=[[INF for i in range(n+1)] for j in range(n+1)]
down_chart=[[INF for i in range(n+1)] for j in range(n+1)]

for i in range(1, n+1):
    up_chart[i][i]=0
    down_chart[i][i]=0

for _ in range(m):
    f, s = map(int, input().split())
    up_chart[f][s]=0
    down_chart[s][f]=0


for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            up_chart[i][j]=min(up_chart[i][j], up_chart[i][k] + up_chart[k][j])
            down_chart[i][j]=min(down_chart[i][j], down_chart[i][k] + down_chart[k][j])
ans=0
for i in range(1, n+1):
    up_cnt=0
    down_cnt=0
    for j in range(1, n+1):
        if up_chart[i][j] == 0:
            up_cnt+=1
        if down_chart[i][j] == 0:
            down_cnt+=1
    if up_cnt + down_cnt == n + 1:
        ans+=1

print(ans)