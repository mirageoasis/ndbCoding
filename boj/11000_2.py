import sys
import heapq

n=int(input())

heap=[]
li=[]

for _ in range(n):
    st, ed=map(int, sys.stdin.readline().split())
    li.append((st, ed))

li.sort(key=lambda x: (x[0], x[1]))
#print(li)
for st, ed in li:
    # ed st순으로 나열
    if not heap:
        heapq.heappush(heap, (ed, st))
    else:
        n_ed, n_st = heap[0]
        if n_ed <= st:
            heapq.heappop(heap)
            heapq.heappush(heap, (ed, n_st))
        else:
            heapq.heappush(heap, (ed, st))


print(len(heap))