N, M = map(int, input().split())
# N은 여행지의 개수, M은 여행할 도시의 수

chart = []
parent = [i for i in range(N)]

def parent_find(parent, i):
    #print(i)
    if parent[i] != i:
        parent[i] = parent_find(parent, parent[i])
    return parent[i]

def union(parent, i, j):
    a = parent_find(parent, i)
    b = parent_find(parent, j)

    if a <= b:
        parent[b] = parent[a]
    else:
        parent[a] = parent[b]

for i in range(N):
    chart.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        if chart[i][j] == 1:
            union(parent, i, j)

# 도시수 입력 받음
route = list(map(int, input().split()))
route = [i-1 for i in route]
route = list(set(route))

idx = parent_find(parent, route[0])

for i in route:
    if parent_find(parent, i) != idx:
        print("NO")
        break
else:
    print("YES")
