import sys
dp=[]
input=sys.stdin.readline
n=int(input())
INF=9999999999
dp=[[INF for i in range(3)] for j in range(n)]
chart=[]
for i in range(n):
    chart.append(list(map(int, input().split())))

def cal(index, pt):
    global INF
    if index == 0:
        dp[index][pt]=chart[index][pt]
        return dp[index][pt]
    if dp[index][pt] != INF:
        return dp[index][pt]

    for i in range(3):
        if i != pt:
            dp[index][pt]=min(dp[index][pt], cal(index-1, i) + chart[index][pt])
    
    return dp[index][pt]

print(min(cal(n-1, 0), cal(n-1, 1), cal(n-1, 2)))