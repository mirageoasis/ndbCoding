'''
7 12
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4
7 3 6
5 1 5
1 6 2
6 4 1
6 5 3
4 5 3
6 7 4
'''

def parent_find(parent, n):
    if parent[n] != n:
        parent[n] = parent_find(parent, parent[n])
    return parent[n]

def union(parent, a, b):
    a_parent = parent_find(parent, a)
    b_parent = parent_find(parent, b)
    if a_parent < b_parent:
        parent[b_parent] = a_parent
    else:
        parent[a_parent] = b_parent

v, e = map(int, input().split())
parent = [0] * (v + 1) # 부모 테이블 초기화

# 모든 간선을 담을 리스트와, 최종 비용을 담을 변수
edges = []
result = 0

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# 모든 간선에 대한 정보를 입력받기
for _ in range(e):
    a, b, cost = map(int, input().split())
    # 비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((cost, a, b))

edges.sort()
edge_list = []
minus = 0
cnt = 1


for i in edges:
    cost, a, b = i
    a_parent =  parent_find(parent, a)
    b_parent =  parent_find(parent, b)

    if a_parent == b_parent:
        continue
    #print(a, b, cost)
    #print(a_parent, b_parent)
    union(parent, a, b)
    #print(parent)
    result+=cost
    minus = cost
    cnt+=1
#print(cnt)

print(result - minus)