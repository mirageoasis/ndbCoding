N = int(input())

dp = [0 for i in range(41)]

dp[1] = 1
dp[2] = 3

for i in range(3, 40):
    dp[i] = (dp[i - 2] * 2 + dp[i - 1])

if N >= 3:
    if N % 2 == 0:
        print((dp[N] - dp[(N - 2) // 2] * 2 - dp[N // 2]) // 2 + dp[(N - 2) // 2] * 2 + dp[N // 2])
    else:
        print((dp[N] - dp[(N - 1) // 2]) // 2 + dp[(N - 1) // 2])
else:
    print(dp[N])