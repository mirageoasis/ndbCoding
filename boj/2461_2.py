import sys
from heapq import heappush, heappop

heap=[]
n, m = map(int, input().split())
chart=[]

for i in range(n):
    chart.append(list(sorted(map(int, sys.stdin.readline().split()))))
maxi=chart[0][0]
mini=chart[0][0]
for i in range(n):
    heappush(heap, (chart[i][0], 0, i))
    maxi=max(maxi, chart[i][0])
    mini=min(mini, chart[i][0])
ans=maxi-mini
now_max=maxi
while True:
    val, idx, chart_idx = heappop(heap)

    if idx == m-1:
        break
    heappush(heap, (chart[chart_idx][idx+1], idx+1, chart_idx))
    now_max=max(chart[chart_idx][idx+1], now_max)
    ans=min(ans, now_max-heap[0][0])
    #print(ans, heap)

print(ans)