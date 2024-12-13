import sys

t=int(input())

div=1000000009

for i in range(t):
    n, m = map(int, sys.stdin.readline().split())
    dp=[[0 for i in range(m+1)] for j in range(n+1)]

    dp[1][1]=1
    if n >=2:
        dp[2][1]=1
        if m >=2:
            dp[2][2]=1
    
    if n>=3:
        dp[3][1]=1
        if m >=2:
            dp[3][2]=2
        if m >=3:
            dp[3][3]=1
    
    for i in range(4, n+1):
        for j in range(2, m+1):
            dp[i][j]=(dp[i-1][j-1] + dp[i-2][j-1] + dp[i-3][j-1]) % div

    ans=0
    for d in dp[n]:
        ans = (ans+d) % div
    print(ans)
    # for d in dp:
    #     print(d)