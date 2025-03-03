import sys
from heapq import heappop, heappush
input=sys.stdin.readline

n=int(input())
chart=[]
for i in range(n):
    chart.append(list(map(int, input().split())))

l, p = map(int, input().split())

chart.sort()
chart.append([l, 0])
heap=[]
ans=0

for dist, oil in chart:
    if dist > p:
        while heap:
            o=heappop(heap)
            o=abs(o)
            p+=o
            ans+=1
            if dist <= p:
                break
        if dist > p:
            break
    heappush(heap, -oil)
    #print(heap)

if p < l:
    print(-1)
else:
    print(ans)