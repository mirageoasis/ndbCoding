import sys
from heapq import heappush, heappop
n, capa = map(int, input().split())
m=int(input())
chart=[]
for i in range(m):
    chart.append(list(map(int, sys.stdin.readline().split())))

# 목적지 따라서 최소 heap
chart.sort(key=lambda x: (x[1], x[0], -x[2]))
maxi_chart=[0 for i in range(n+1)]

ans=0
maxi=0
for s,e,val in chart:
    temp_max=val
    for j in range(s, e):
        temp_max = min(capa-maxi_chart[j], temp_max)
    
    for j in range(s, e):
        maxi_chart[j]+=temp_max
    ans+=temp_max

print(ans)