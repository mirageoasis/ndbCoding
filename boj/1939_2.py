import sys
import heapq
land_number, bridge_number = map(int, input().split())
INF=1_000_000_001

graph=[[] for _ in range(land_number+1)]
weight=[0 for _ in range(land_number+1)]

for _ in range(bridge_number):
    start, end, w = map(int, sys.stdin.readline().split())
    graph[start].append((w, end))
    graph[end].append((w, start))

start, end = map(int, input().split())

weight[start]=INF
que=[]
que.append((-INF, start))


while que:
    now_weight, now_point = heapq.heappop(que)
    now_weight=-now_weight

    if weight[now_point] > now_weight:
        continue

    for new_weight, new_point in graph[now_point]:
        new_weight = min(new_weight, now_weight)
        if weight[new_point] < new_weight:
            weight[new_point]=new_weight
            heapq.heappush(que, (-new_weight, new_point))

print(weight[end])