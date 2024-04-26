from collections import deque

N = int(input())
chart = list(map(int, input().split()))
s = int(input())

graph = [[] for i in range(N)]
visited = [False for i in range(N)]

for idx, val in enumerate(chart):
    left = idx - val 
    right = idx + val

    if left > -1:
        graph[idx].append(left)
    
    if right < N:
        graph[idx].append(right)
    

# for i in graph:
#     print(i)

def bfs(s, graph, visited):
    visited[s] = True
    q = deque()
    q.append(s)

    while q:
        v = q.popleft()

        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
    

bfs(s - 1, graph, visited)

print(visited.count(True))