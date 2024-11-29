import sys

T=int(input())

for _ in range(T):
    l, n = map(int, sys.stdin.readline().split())
    chart=[]
    for i in range(n):
        chart.append(int(sys.stdin.readline().strip()))
    mi=[]
    ma=[]
    for c in chart:
        mi.append(min(l-c, c))
        ma.append(max(l-c, c))
    
    mi.sort()
    ma.sort()

    print(mi[-1], ma[-1])