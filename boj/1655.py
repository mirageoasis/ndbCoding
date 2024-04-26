import heapq
import sys

N = int(input())

small = []
big = []

mid = int(input())
print(mid)

for i in range(N - 1):
    num = int(sys.stdin.readline())

    # mid는 

    if num < mid:
        heapq.heappush(small, -num)
    else:
        heapq.heappush(big, num)
    
    if len(big) - len(small) == 2:
        t = heapq.heappop(big)
        heapq.heappush(small, -mid)
        mid = t
    elif len(small) - len(big) == 1:
        t = -heapq.heappop(small)
        heapq.heappush(big, mid)
        mid = t


    print(mid)



