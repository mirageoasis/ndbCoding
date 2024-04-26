import sys
import heapq

N = int(input())

li = []

for i in range(N):
    li.append(list(map(int, sys.stdin.readline().strip().split(' '))))

li.sort(key=lambda x : (x[0], x[1]))


if len(li) > 1:

    heap = [li[0][1]]

    for start, end in li[1:]:
        t = heap[0]
        if start >= t:
            heapq.heappop(heap)
        heapq.heappush(heap, end)
    
    print(len(heap))
else:
    print(1)