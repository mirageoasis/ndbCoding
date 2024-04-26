N, K = map(int, input().split())

chart = [[0 for i in range(N+1)] for j in range(N+1)]

for i in range(N+1):
    for j in range(0, i+1):
        if j == 0 or j == i:
            chart[i][j] = 1
        else:
            chart[i][j] = (chart[i - 1][j] + chart[i - 1][j - 1]) % 10007


print(chart[N][K])