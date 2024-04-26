import sys
sys.setrecursionlimit(1000001)

N = int(input())

li = []

graph = [[] for i in range(N+1)]
visited = [False for i in range(N+1)]
dp = [[1, 0] for i in range(N+1)]

def dfs(num):
    # 첫번째는 내가 adapter, 두번째는 나는 follower
    visited[num] = True
    
    for i in graph[num]:
        if visited[i]:
            continue
        dfs(i)
        dp[num][0] += min(dp[i][0], dp[i][1])
        dp[num][1] += dp[i][0]


for i in range(N-1):
    a, b =map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)


dfs(1)

print(min(dp[1][0], dp[1][1]))