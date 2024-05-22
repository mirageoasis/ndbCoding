import sys

n, m = map(int, input().split())

chart = []

for i in range(n):
    chart.append(int(sys.stdin.readline()))

sum = [0] * (n + 1)
for i in range(1, n + 1):
    sum[i] = chart[i - 1] + sum[i - 1]

dp = [[0] * (m + 1) for _ in range(n + 1)]
for j in range(1, m + 1):
    dp[0][j] = -4000000

for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = dp[i - 1][j]
        for k in range(1, i + 1):
            if k >= 2:
                dp[i][j] = max(dp[i][j], dp[k - 2][j - 1] + sum[i] - sum[k - 1])
            elif k == 1 and j == 1:
                dp[i][j] = max(dp[i][j], sum[i])

print(dp[n][m])