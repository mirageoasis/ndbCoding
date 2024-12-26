import sys
from heapq import heappush, heappop


n=int(input())
mid=0

small_heap=[] # 최대 값 -> minus 처리
big_heap=[] # 최소 값

for i in range(n):
    num=int(sys.stdin.readline())
    if i == 0:
        print(num)
        mid=num
        continue
    
    if num >= mid:
        heappush(big_heap, num)
    else:
        heappush(small_heap, -num)
    
    # 중간 계산
    if(len(small_heap) > len(big_heap)):
        heappush(big_heap, mid)
        mid=-heappop(small_heap)
    else:
        if (len(small_heap) + 1 < len(big_heap)):
            heappush(small_heap, -mid)
            mid=heappop(big_heap)
    
    print(mid)

