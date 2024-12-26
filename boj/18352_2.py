import sys
from heapq import heappush, heappop
from collections import deque
INF=9999999
city_cnt, num_street, target_dist, start_loc = map(int, input().split())

graph=[[] for i in range(city_cnt+1)]
visit=[False for i in range(city_cnt+1)]
dist=[INF for i in range(city_cnt+1)]

for _ in range(num_street):
    start, end = map(int, sys.stdin.readline().split())
    graph[start].append(end)



def djk():
    global city_cnt, num_street, start_loc, graph, dist
    heap=[]
    heappush(heap, (0, start_loc))
    dist[start_loc]=0
    while heap:
        now_dist, pt = heappop(heap)
        if now_dist > dist[pt]:
            continue
        
        for i in graph[pt]:
            new_dist=now_dist+1
            if dist[i] > new_dist:
                dist[i]=new_dist
                heappush(heap, (new_dist, i))

djk()
#print(dist)
if not dist.count(target_dist):
    print(-1)
else:
    for i in range(city_cnt+1):
        if dist[i] == target_dist:
            print(i)
