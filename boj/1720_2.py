dp=[0 for i in range(42)]

n=int(input())

dp[1]=1
dp[2]=3

for i in range(3, 42):
    dp[i] = dp[i-1] + dp[i-2]*2

clone_dp=[0 for i in range(42)]

clone_dp[0]=0
clone_dp[1]=1
clone_dp[2]=3

for i in range(3, 42):
    if i % 2 == 0:
        clone_dp[i] = dp[i//2] + dp[i//2 - 1] * 2
    else:
        clone_dp[i] = dp[i//2]
    
#print(dp[n], clone_dp[n])
print((dp[n] + clone_dp[n]) // 2)