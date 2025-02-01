from heapq import heappop, heappush
n, m = map(int, input().split())
li = map(int, input().split())

heap=[]

for i in li:
    heappush(heap, i)

for i in range(m):
    first=heappop(heap)
    second=heappop(heap)
    res=first+second
    heappush(heap, res)
    heappush(heap, res)

print(sum(heap))