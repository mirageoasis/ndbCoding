from collections import deque
from collections import defaultdict

deq = deque()

# 도시개수, 반복문, 최단거리, 출발도시
N, M, K, X = map(int ,input().split())

chart = defaultdict(list)
visited = [False] * (N + 1)
distance = [0] * (N + 1)

for _ in range(M):
    a, b = map(int ,input().split())
    chart[a].append(b)

deq.append((X, 0))
visited[X] = True

while deq:
    point, dist = deq.popleft()
    distance[point] = dist
    #print("point dist")
    #print(point, dist)
    for i in chart[point]:
        if not visited[i]:
            visited[i] = True
            deq.append((i, dist + 1))

ans = []

for idx ,i in enumerate(distance):
    if i == K:
        ans.append(idx)

#print(ans)

if len(ans) == 0:
    print(-1)
else:
    for i in ans:
        print(i)