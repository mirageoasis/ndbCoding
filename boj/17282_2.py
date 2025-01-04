n, start = map(int, input().split())
chart=[]
for i in range(n):
    chart.append(list(map(int, input().split())))

for k in range(n):
    for i in range(n):
        for j in range(n):
            chart[i][j] = min(chart[i][k] + chart[k][j], chart[i][j])

visit=[False for i in range(n)]
ans=9999999999
def backtrack(now, idx, dist):
    global n, visit, chart, ans
    if idx == n-1:
        ans=min(ans, dist)
        return
    
    for i in range(n):
        if not visit[i]:
            visit[i]=True
            backtrack(i, idx+1, dist+chart[now][i])
            visit[i]=False

visit[start]=True
backtrack(start, 0, 0)

print(ans)