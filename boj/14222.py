# 52분 시작
from heapq import heapify, heappop, heappush

N, K = map(int, input().split())
chart = list(map(int, input().split()))
chart.sort()


now=1
heapify(chart)

while chart:
    num=chart[0]
    if num == now:
        heappop(chart)
        now+=1
    elif num < now:
        heappop(chart)
        heappush(chart, num+K)
    else:
        break

#print(chart)

if not chart:
    print(1)
else:
    print(0)