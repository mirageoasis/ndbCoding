import sys
input=sys.stdin.readline

n, m = map(int, input().split())
chart=[]

for i in range(n):
    chart.append(list(map(int, input().strip().split())))

for k in range(n):
    for i in range(n):
        for j in range(n):
            chart[i][j] = min(chart[i][k] + chart[k][j], chart[i][j])


for _ in range(m):
    a, b, c = map(int, input().strip().split())
    a-=1
    b-=1
    if chart[a][b] > c:
        print("Stay here")
    else:
        print("Enjoy other party")
