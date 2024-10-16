N, E = map(int, input().split())
# (점, 거리 방식으로 할꺼임)
INF=999999999999

graph=[[INF for i in range(N+1)] for j in range(N+1)]
parent = [i for i in range(N+1)]
# parent find 방식으로 체크할까?

def parent_find(x):
    if parent[x] != x:
        parent[x] = parent_find(parent[x])
    return parent[x]

def union(a, b):
    a_parent = parent_find(a)
    b_parent = parent_find(b)

    if a_parent < b_parent:
        parent[b_parent] = a_parent
    else:
        parent[a_parent] = b_parent
graph[1][1]=0
for i in range(E):
    st, ed, d = map(int, input().split())
    #graph[st].append((ed, d))
    #graph[ed].append((st, d))
    graph[st][ed]=d
    graph[ed][st]=d
    union(st, ed)

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


v1, v2 = map(int, input().split())

#print(graph)

if (1 != parent_find(v1) and 1 != parent_find(v2)) or 1 != parent_find(N):
    print(-1)
else:
    # 1~v1
    # 1~v2
    # v1~v2
    # v1~N
    # v2~N
    first=INF
    second=INF
    if v2 == N:
        first=graph[1][v1]+graph[v1][N]
    else:
        first=graph[1][v1]+graph[v1][v2]+graph[v2][N]

    if v1 == 1:
        second=graph[1][v2]+graph[v2][N]
    else:
        second=graph[1][v2]+graph[v2][v1]+graph[v1][N]

    ans=min(first, second)
    print(ans)