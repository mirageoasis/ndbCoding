import sys
from heapq import heappush, heappop

N, K = map(int, input().split())

gems=[]
bags=[]

for i in range(N):
    gems.append(tuple(map(int, sys.stdin.readline().split())))

for i in range(K):
    bags.append(int(sys.stdin.readline()))

bags.sort()
# 무게로 sort
gems.sort(key=lambda x: x[0])
# heap추가
# 무게만 heappush
heap=[]

# 가방 무게 고려
ans=0
idx=0
for bag in bags:
    while idx < len(gems) and gems[idx][0] <= bag:
        heappush(heap, -gems[idx][1])
        idx+=1
    if len(heap):
        ans+=abs(heappop(heap))

print(ans)