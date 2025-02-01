import sys
n,m=map(int, input().split())
chart=[]
s=[[0 for i in range(n+1)]for j in range(n+1)]
cmd=[]
for i in range(n):
    chart.append(list(map(int, sys.stdin.readline().split())))

for i in range(m):
    cmd.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, n+1):
    for j in range(1,n+1):
        s[i][j] = chart[i-1][j-1]

for i in range(1, n+1):
    for j in range(1,n+1):
        s[i][j] += s[i][j-1]
for i in range(1, n+1):
    for j in range(1,n+1):
        s[i][j] += s[i-1][j]

for c in cmd:
    a1, a2, b1, b2 = c
    print(s[b1][b2] + s[a1-1][a2-1] - s[b1][a2-1] - s[a1-1][b2])