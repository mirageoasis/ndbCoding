from heapq import heappush, heappop
from collections import defaultdict

N, M = map(int, input().split())
INF = 999999999999

visited = [False for i in range(N+1)]
distance = [INF for i in range(N+1)]
connected = defaultdict(list)

# (distance, idx 표기)

for _ in range(M):
    start, fin = map(int, input().split())
    connected[start].append((1, fin))
    connected[fin].append((1, start))

cnt=0

que = []
# distance, idx 구성
heappush(que, (0, 1))
distance[1] = 0


while cnt<N:
    d, idx = heappop(que)

    # 굳이 visited 처리를 안하고 현재 distance 보다 길다면 return 하는 방식도 존재한다.
    if (visited[idx] == True):
        continue

    for d, i in connected[idx]:
        # distance[idx] 현재 노드 + idx 기준 거리 
        distance[i] = min(distance[i], distance[idx] + d)
        heappush(que, (distance[i], i))
    visited[idx] = True
    cnt+=1

print(distance)
distance[1] = INF
for i in range(N+1):
    if distance[i] == INF:
        distance[i] = -1

print(distance.index(max(distance)), max(distance),distance.count(max(distance)))