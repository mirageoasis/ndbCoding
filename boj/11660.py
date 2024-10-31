import sys

n, m = map(int, input().split())
sum_chart=[]
chart=[]
res=[]

for i in range(n):
    chart.append(list(map(int, sys.stdin.readline().split())))

# 합 차트 작성 시작

sum_chart.append([0 for i in range(n+1)])
for i in range(n):
    sum_chart.append([0] + chart[i])

# for c in sum_chart:
#     print(c)

# 가로
for i in range(1, n+1):
    for j in range(1, n+1):
        sum_chart[i][j]+=sum_chart[i][j-1]

for i in range(1, n+1):
    for j in range(1, n+1):
        sum_chart[i][j]+=sum_chart[i-1][j]

for i in range(m):
    a, b, c, d = map(int, sys.stdin.readline().split())
    print(sum_chart[c][d] + sum_chart[a-1][b-1] - sum_chart[c][b-1] - sum_chart[a-1][d])
