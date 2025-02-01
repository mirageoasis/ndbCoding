n=int(input())

li=[]
import sys
for i in range(n):
    li.append(list(map(int, sys.stdin.readline().split())))

li.sort(key=lambda x: x[0])
from heapq import heappush, heappop
heap=[]
for deadline, value in li:
    if not heap:
        heappush(heap, (value, deadline))
        continue
    if len(heap) >= deadline:
        if heap[0][0] < value:
            heappop(heap)
            heappush(heap, (value, deadline))
    else:
        heappush(heap, (value, deadline))
#print(heap)
print(sum([v for v, d in heap]))
