from collections import deque

li = []# 연결된 노드 개수
graph = [] # 인접 리스트

q = deque()

q.append(0)

while q:
    idx = q.popleft()
    for i in graph[idx]:
        li[i] -= 1
        if li[i] == 0:
            q.append(i)