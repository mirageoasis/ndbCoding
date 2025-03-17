import sys
input=sys.stdin.readline
sys.setrecursionlimit(100000)
n=int(input())
chart=[]

for i in range(n):
    chart.append(list(map(int, input().split())))

chart.insert(0, (0, 0))
dp=[0 for i in range(n+1)]
visit=[False for i in range(n+1)]
# 0 1 2 3 4

for i in range(1, n+1):
    t, p = chart[i]
    dp[i]=max(dp[i], dp[i-1])
    if i + t - 1 <= n:
        dp[i+t-1]=max(dp[i+t-1], dp[i-1] + p)

#print(dp)
print(dp[n])