import heapq
import sys

N=int(input())

heap=[]

for i in range(N):
    nums=map(int, sys.stdin.readline().strip().split())
    #print(nums)
    for num in nums:
        if len(heap) < N:
            heapq.heappush(heap, num)
        else:
            heapq.heappush(heap, num)
            heapq.heappop(heap)

print(heapq.heappop(heap))