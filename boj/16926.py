n, m, times = map(int, input().split())

graph=[]
for i in range(n):
    graph.append(list(map(int, input().split())))
from copy import deepcopy
# 귀찮은데...

# 꼭지점에서 출발
# 왼위, 오위, 왼아, 오아

new_graph=graph

def cal():
    global left_up, left_down, right_up, right_down, new_graph, graph, n, m, times
    cnt=0
    new_graph=deepcopy(graph)
    left_up = [0, 0]
    right_up = [0, m-1]

    left_down = [n-1, 0]
    right_down = [n-1, m-1]
    #times%=(m+n-2)*2

    from collections import deque
    while True:
        #print(left_up, right_up)
        #print(left_down, left_up)
        #print()
        ring=deque()
        
        for i in range(left_up[0], left_down[0]):
            ring.append(graph[i][left_up[1]])
        for i in range(left_down[1], right_down[1]):
            ring.append(graph[left_down[0]][i])
        for i in range(right_down[0], right_up[0], -1):
            ring.append(graph[i][right_down[1]])
        for i in range(right_up[1], left_up[1], -1):
            ring.append(graph[right_up[0]][i])

        #print(ring)
        for i in range(times):
            ring.appendleft(ring.pop())
        #print(ring)
        idx=0
        for i in range(left_up[0], left_down[0]):
            new_graph[i][left_up[1]]=ring[idx]
            idx+=1
        for i in range(left_down[1], right_down[1]):
            new_graph[left_down[0]][i]=ring[idx]
            idx+=1
        for i in range(right_down[0], right_up[0], -1):
            new_graph[i][right_down[1]]=ring[idx]
            idx+=1
        for i in range(right_up[1], left_up[1], -1):
            new_graph[right_up[0]][i]=ring[idx]
            idx+=1

        left_up=[left_up[0]+1, left_up[1]+1]
        right_up=[right_up[0]+1, right_up[1]-1]
        left_down=[left_down[0]-1, left_down[1]+1]
        right_down=[right_down[0]-1, right_down[1]-1]
        cnt+=1
        if cnt >= min(n, m) // 2:
            break
    graph=deepcopy(new_graph)

#cal()
cal()

for g in new_graph:
    print(*g)
#print()