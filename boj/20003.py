import sys

T = int(input())

for i in range(T):
    chart = []
    n, m = map(int, sys.stdin.readline().strip().split())
    for _ in range(m+1):
        chart.append([0 for j in range(n+4)])

    chart[1][1] = 1
    chart[1][2] = 1
    chart[1][3] = 1

    if m >= 2:
        chart[2][1] = 0
        chart[2][2] = 1
        chart[2][3] = 2
    if m >= 3:
        chart[3][1] = 0
        chart[3][2] = 0
        chart[3][3] = 1
    
    for j in range(2, m+1):
        for k in range(4, n+4):
            chart[j][k] = (chart[j-1][k-1] + chart[j-1][k-2] + chart[j-1][k-3]) % 1000000009
    
    t = [j[-4] for j in chart ]
    print(sum(t) % 1000000009)