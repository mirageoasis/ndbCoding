N = int(input())

dp = [True for i in range(N+100)]

# 0 선공 lose

dp[1] = False
dp[2] = True
dp[3] = False
dp[4] = True

for i in range(5, N+1):
    if dp[i - 1] and dp[i - 3] and dp[i - 4]:
        dp[i] = False


print("SK" if dp[N] else "CY")