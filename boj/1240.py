import sys
from collections import deque
from heapq import heappop, heappush

input=sys.stdin.readline

n, m = map(int, input().split())
INF=99999999
chart=[[] for j in range(n+1)]
dist=[[INF for i in range(n+1)] for j in range(n+1)]

for i in range(n-1):
    start, end, d = map(int, input().split())
    chart[start].append((d, end))
    chart[end].append((d, start))

def cal(start):
    global dist
    dist[start][start]=0
    heap=[]
    heappush(heap, (0, start))
    while heap:
        d, p = heappop(heap)
        if d > dist[start][p]:
            continue
        
        for new_d, new_p in chart[p]:
            new_dist = new_d + d
            if dist[start][new_p] >= new_dist:
                dist[start][new_p]=new_dist
                heappush(heap, (new_dist, new_p))

for i in range(1, n+1):
    cal(i)

for i in range(m):
    start, end = map(int, input().split())
    print(dist[start][end])