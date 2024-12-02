import sys


n, m = map(int, input().split())
enemy=[i for i in range(n+1)]
parent=[i for i in  range(n+1)]


def parent_find(a):
    if parent[a] != a:
        parent[a]=parent_find(parent[a])
    return parent[a]

def union(a, b):
    a=parent_find(a)
    b=parent_find(b)

    if a < b:
        parent[b]=a
    else:
        parent[a]=b


ans=True
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())

    a_p = parent_find(a)
    b_p = parent_find(b)

    if a_p == b_p:
        ans=False
        break

    if enemy[a] == a:
        enemy[a]=b
    else:
        union(enemy[a], b)
    
    if enemy[b] == b:
        enemy[b]=a
    else:
        union(enemy[b], a)
    

print(1 if ans else 0)