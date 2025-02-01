from heapq import heappush, heappop
n=int(input())
heap=[]
import sys
for _ in range(n):
    li=list(map(int, sys.stdin.readline().split()))
    for j in li:
        num=j
        heappush(heap, num)
        if len(heap) > n:
            heappop(heap)    
#print(heap)
print(heap[0])