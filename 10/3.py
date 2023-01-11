from collections import deque
import copy
'''
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1
'''

# 노드의 개수 입력받기
v = int(input())
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v + 1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트(그래프) 초기화
graph = [[] for i in range(v + 1)]
# 각 강의 시간을 0으로 초기화
time = [0] * (v + 1)

ans = time.copy()

# 방향 그래프의 모든 간선 정보를 입력받기
for i in range(1, v + 1):
    data = list(map(int, input().split()))
    time[i] = data[0] # 첫 번째 수는 시간 정보를 담고 있음
    for x in data[1:-1]:
        indegree[i] += 1
        graph[x].append(i)

q = deque()

for i in range(1,v+1):
    if indegree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()

    for i in graph[now]:
        indegree[i] -= 1
        ans[i] = max(ans[i], result[now] + time[i])
        if indegree[i] == 0:
            q.append(i)

for i in range(1, v+1):
    print(ans[i])