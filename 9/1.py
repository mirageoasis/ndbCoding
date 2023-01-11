from heapq import heappush, heappop

heap = []

heappush(heap, (1, 2))
heappush(heap, (1, 3))
heappush(heap, (1, 1))

print(heappop(heap))
print(heappop(heap))
print(heappop(heap))