import sys

n, m, q = map(int, input().split())

chart=[[0 for i in range(m)] for j in range(n)]

col=[0 for i in range(m)]
row=[0 for j in range(n)]

for i in range(q):
    c, r ,v = map(int, sys.stdin.readline().split())
    r-=1
    if c == 1:
        row[r]+=v
    else:
        col[r]+=v

for i in range(n):
    for j in range(m):
        chart[i][j]+=row[i]


for j in range(m):
    for i in range(n):
        chart[i][j]+=col[j]

for i in range(n):
    print(*chart[i])
