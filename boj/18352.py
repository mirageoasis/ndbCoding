from collections import deque
import heapq

N, M, K, X = map(int, input().split(' '))

INF = 1000000000

graph = [[] for i in range(N+1)]
visited = [False for i in range(N+1)]
distance_chart = [INF for i in range(N+1)]

distance_chart[X] = 0
visited[X] = True
ans = []
heap = []

for i in range(M):
    a, b = map(int, input().split(' '))
    graph[a].append(b)
    if a == X:
        heapq.heappush(heap, (1, b))
        distance_chart[b] = 1


while heap:
    distance, point = heapq.heappop(heap)

    if distance_chart[point] < distance:
        continue

    for p in graph[point]:
        if distance + 1 < distance_chart[p]:
            heapq.heappush(heap, (distance+1, p))
            distance_chart[p] = distance + 1

ans = [idx for idx, dist in enumerate(distance_chart) if dist == K]

if ans:
    for i in ans:
        print(i)
else:
    print(-1)