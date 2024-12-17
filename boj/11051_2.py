n, m = map(int, input().split())

chart=[[1 for i in range(1001)] for j in range(1001)]


for i in range(1, 1001):
    for j in range(1, i):
        chart[i][j] = (chart[i-1][j-1] + chart[i-1][j]) % 10007
    

print(chart[n][m])
