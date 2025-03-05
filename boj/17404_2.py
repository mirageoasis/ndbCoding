import sys
dp=[]
input=sys.stdin.readline
n=int(input())
INF=9999999999
dp=[[INF for i in range(3)] for j in range(n)]
chart=[]
for i in range(n):
    chart.append(list(map(int, input().split())))

def cal(index, pt, start):
    global INF
    if index == 0:
        if pt != start:
            dp[index][pt]=chart[index][pt]
            return dp[index][pt]
        else:
            return INF
    if dp[index][pt] != INF:
        return dp[index][pt]

    for i in range(3):
        if i != pt:
            dp[index][pt]=min(dp[index][pt], cal(index-1, i, start) + chart[index][pt])
    
    return dp[index][pt]
ans=INF
ans=min(cal(n-1, 0, 0), ans)
dp=[[INF for i in range(3)] for j in range(n)]
ans=min(cal(n-1, 1, 1), ans)
dp=[[INF for i in range(3)] for j in range(n)]
ans=min(cal(n-1, 2, 2), ans)
print(ans)