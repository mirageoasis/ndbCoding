import sys
from heapq import heappush, heappop

input=sys.stdin.readline

def bfs(start):
    global d, graph, dist, n
    
    if d[start][0] == 'T':
        return
    # 돈, 점
    heap=[(0, 1)]
    #dist[1]=0

    while heap:
        old_dist, pt = heappop(heap)
        old_dist=old_dist * -1
        cost = d[pt][1]
        if d[pt][0] == 'T':
            old_dist -= cost
        else:
            old_dist = max(old_dist, cost)
        #print(pt, old_dist, cost)
        if dist[pt] >= old_dist:
            continue
        if old_dist < 0:
            continue
        if pt == n:
            dist[pt]=old_dist
            break
        dist[pt]=old_dist
        
        for new_pt in graph[pt]:
            if old_dist > dist[new_pt]:
                heappush(heap, (-old_dist, new_pt))


while True:
    n=int(input())
    if not n:
        break
    graph=[[] for i in range(n+1)]
    dist=[-1 for i in range(n+1)]
    d=dict()
    for i in range(1,n +1):
        li = input().split()
        alpha = li[0]
        li=list(map(int, li[1:]))
        cost = li[0]
        li=li[1:]
        li.pop()
        graph[i]=li
        d[i]=(alpha, cost)
    bfs(1)
    
    #print(graph)
    #print(d)
    #print(dist)
    if dist[-1] > -1:
        print("Yes")
    else:
        print("No")
