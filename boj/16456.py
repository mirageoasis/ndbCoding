n=int(input())

dp=[0 for i in range(50001)]

dp[0]=1
dp[1]=1
dp[2]=1
dp[3]=2
dp[4]=dp[1] + dp[3] 

for i in range(5, 50001):
    dp[i] = (dp[i-3] + dp[i-1]) % 1000000009

print(dp[n])