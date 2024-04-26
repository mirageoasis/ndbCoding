# 3:48
# N^N은 안된다.
# 다익스트라 변형
#

import sys
from heapq import heappush, heappop

N, M = map(int, sys.stdin.readline().split())
# distance, point 순으로 되어있다.
graph = [[] for i in range(N+1)]

def djk(start, end, graph, N):
    weight_chart = [-1 for i in range(N+1)]
    weight_chart[start] = 1000000001
    #print(weight_chart)
    heap = []
    
    heappush(heap, (weight_chart[start], start))
    while heap:
        weight, point = heappop(heap)
        # 원래 있던 친구가 작다면(무게가 무겁다면 continue)
        if weight_chart[point] > abs(weight):
            continue
        
        for weight_to_go, new_point in graph[point]:
            # 지금까지 유지했던 거리보다, 지나려는 교량의 거리가 크다면(무게가 가볍다면) 갱신
            #print(weight_to_go, weight_chart[point], weight_chart[new_point], new_point)
            #print(new_point, start)
            new_weight = min(abs(weight_to_go), weight_chart[point])
            if new_point != start and weight_chart[new_point] < new_weight:
                weight_chart[new_point] = new_weight
                heappush(heap, (-new_weight, new_point))
    return weight_chart[end]

temp_dict=dict()

for i in range(M):
    s, e, weight = map(int, sys.stdin.readline().split())
    start = min(s, e)
    end = max(s, e)
    if (start, end) not in temp_dict:
        temp_dict[(start, end)] = (start, end, weight)
    else:
        n_s, n_e, n_w = temp_dict[(start, end)]
        if n_w < weight:
            temp_dict[(start, end)] = (start, end, weight)



for start, end, weight in temp_dict.values():
    graph[start].append((-weight, end))
    graph[end].append((-weight, start))

start, end = map(int, sys.stdin.readline().split()) 

print(djk(start, end, graph, N))
