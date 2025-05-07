import sys
from heapq import heappush, heappop
input=sys.stdin.readline
INF=9999999999
v, e = map(int, input().split())

start=int(input())

graph=[dict() for i in range(v+1)]
dist=[INF for i in range(v+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    if graph[a].get(b) is None:
        graph[a][b] = c
    else:
        if c < graph[a][b]:
            graph[a][b]=c
    
def djk():
    global start, v, e, graph
    dist[start]=0
    heap=[]
    heappush(heap, (0, start))
    while heap:
        d, pt = heappop(heap)
        if d > dist[pt]:
            continue
        for key, value in graph[pt].items():
            new_d = value + d
            if new_d <= dist[key]:
                heappush(heap, (new_d, key))
                dist[key]=new_d
djk()
for i in range(1, v+1):
    if dist[i] == INF:
        print("INF")
    else:
        print(dist[i])