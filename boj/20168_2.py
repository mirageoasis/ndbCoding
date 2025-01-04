import sys
n, m, start, end, money=map(int, input().split())
# visit으로 기록하고 싹다 찾으면 될 듯?
# n이 10이라서 brute force로 가능할 듯

# 수도 작아서 인접 그래프로 안해도 될듯
# 
INF=999999
start-=1
end-=1
chart=[[INF for i in range(n)] for j in range(n)]

for i in range(m):
    a,b,c=map(int, sys.stdin.readline().split())
    a-=1
    b-=1
    chart[a][b]=c
    chart[b][a]=c

visit=[False for i in range(n)]
ans=INF
def dfs(now, now_budget, maxi):
    global n, m, INF, start, end, chart, visit, ans
    # 예산 안되면 앞에서 거른다.
    if now == end:
        #print(f"ans: {maxi}")
        ans=min(maxi, ans)
        return
    
    for future in range(n):
        if chart[now][future] != INF and not visit[future]:
            if now_budget >= chart[now][future]:
                visit[future]=True
                dfs(future, now_budget - chart[now][future], max(maxi, chart[now][future]))
                visit[future]=False


dfs(start, money, 0)

print(-1 if ans == INF else ans)