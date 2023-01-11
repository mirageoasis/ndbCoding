'''
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1

'''

def parent_find(parent, n):
    if n != parent[n]:
        parent[n] = parent_find(parent, parent[n])
    return parent[n]

def union(a, b, parent):
    a_parent = parent_find(parent, a)
    b_parent = parent_find(parent, b)
    if a_parent < b_parent:
        parent[b] = a_parent
    else:
        parent[a] = b_parent


n, m = map(int, input().split())
parent = [0] * (n + 1) # 부모 테이블 초기화

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(0, n + 1):
    parent[i] = i

for i in range(m):
    t, a, b = map(int ,input().split())
    if t == 0:
        union(a, b, parent)
    elif t == 1:
        if parent_find(parent, a) != parent_find(parent, b):
            print("NO")
        else:
            print("YES")
