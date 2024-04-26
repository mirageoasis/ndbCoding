import sys

# 간선의 정보가 다르다. 또한 시간 복잡도는 크게 문제가 되는 것 같지 않다.
# 그리고 최소한의 움직임으로 가는 것이 아니므로 dfs를 사용해야 할 것 같음

N, M, A, B, C = map(int, input().split())

cost_graph = [[0 for i in range(N + 1)] for j in range(N + 1)]
graph = [[] for i in range(N + 1)]
visited = [False for i in range(N + 1)]

for i in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    cost_graph[a][b] = c
    cost_graph[b][a] = c
    graph[a].append(b)
    graph[b].append(a)

ans = 1000000

def dfs(N, now, end, left, maxi, graph, cost_graph, visited):
    if now == end:
        global ans
        ans = min(ans, maxi)

    for i in graph[now]:
        
        if not visited[i] and left >= cost_graph[now][i]:
            visited[i] = True
            dfs(N, i, end, left - cost_graph[now][i], max(maxi, cost_graph[now][i]), graph, cost_graph, visited)
            visited[i] = False



visited[A]=True
dfs(N, A, B, C, 0, graph, cost_graph, visited)

print(ans if ans != 1000000 else -1)