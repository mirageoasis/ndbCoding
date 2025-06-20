import sys
from heapq import heappush, heappop

input=sys.stdin.readline

def bfs(start):
    global d, graph, cost_chart, n
    
    if d[start][0] == 'T':
        return
    # 돈, 점
    heap=[(0, 1)]
    #dist[1]=0

    while heap:
        cost, pt = heappop(heap)
        cost=cost * -1
        point_cost = d[pt][1]
        if d[pt][0] == 'T':
            cost -= point_cost
        else:
            cost = max(cost, point_cost)
        #print(pt, old_dist, cost)
        if cost_chart[pt] >= cost:
            continue
        if cost < 0:
            continue
        if pt == n:
            cost_chart[pt]=cost
            break
        cost_chart[pt]=cost
        
        for new_pt in graph[pt]:
            if cost > cost_chart[new_pt]:
                heappush(heap, (-cost, new_pt))


while True:
    n=int(input())
    if not n:
        break
    graph=[[] for i in range(n+1)]
    cost_chart=[-1 for i in range(n+1)]
    d=dict()
    for i in range(1,n +1):
        li = input().split()
        alpha = li[0]
        li=list(map(int, li[1:]))
        c = li[0]
        li=li[1:]
        li.pop()
        graph[i]=li
        d[i]=(alpha, c)
    bfs(1)
    
    #print(graph)
    #print(d)
    #print(dist)
    if cost_chart[-1] > -1:
        print("Yes")
    else:
        print("No")
