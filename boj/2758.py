n=int(input())

for _ in range(n):
    n, m = map(int, input().split())
    # dp[x][y] -> x일 때 숫자 y개를 사용해서 만드는거
    dp=[[0 for i in range(n+1)] for j in range(m+1)]
    for i in range(0, m+1):
        dp[i][0]=1

    # i - 1 앞에 i//2 에서 -1
    for i in range(1, m+1):
        for j in range(1, n+1):
            dp[i][j]=dp[i-1][j]+dp[i//2][j-1]
    #print(dp)
    print(dp[m][n])