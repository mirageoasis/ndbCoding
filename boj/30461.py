import sys
input=sys.stdin.readline

n, m, q = map(int, input().split())
chart=[]
dp=[]

for i in range(n):
    chart.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(m):
        chart[i][j]+=chart[i-1][j]

for i in range(1, n):
    for j in range(1, m):
        chart[i][j]+=chart[i-1][j-1]

for i in range(q):
    a, b = map(int, input().split())
    a-=1
    b-=1
    ans=0
    print(chart[a][b])
