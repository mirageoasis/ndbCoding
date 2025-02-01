'''
딱봐도 그리디
어떻게 할 것인가?

가치가 높은 순
현재 가능한 가방의 무게 vs 보석 무게
가치 있고, 가벼운 순으로 나열
bisect_left. 
실행할 때 마다 순서가 변해서 이진탐색은 ㄴㄴ
heap은 아닌거 같고

1 65
2 99 -> 여기 까지 진행. 무게는 기억할 필요 x
5 23 -> 10이면 여기 까지 진행
'''
import sys
from heapq import heappush, heappop

n, k = map(int, input().split())
gems=[]
bags=[]
visit=[False for i in range(k)]
for i in range(n):
    gems.append(list(map(int, sys.stdin.readline().split())))
for i in range(k):
    bags.append(int(sys.stdin.readline()))
# 가치가 높고, 무게가 낮은 순서대로
gems.sort(key=lambda x: (x[0], -x[1]))
bags.sort()
ans=0
#print(gems)
# gem heap
heap=[]

# 가방을 순회한다.
gems_idx=0
for bag in bags:
    # 내 bag에 담을 수 있는 무게까지 전부 탐색
    while gems_idx < len(gems):
        if gems[gems_idx][0] <= bag:
            heappush(heap, -gems[gems_idx][1])
        else:
            break
        gems_idx+=1
    #print(gems_idx)
    # 가장 가치있는 친구 pop
    if heap:
        val=heappop(heap)
        ans+=abs(val)

print(ans)