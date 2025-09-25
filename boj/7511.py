import sys
input=sys.stdin.readline
t=int(input())

def parent_find(parent, target):
    if parent[target] != target:
        parent[target] = parent_find(parent, parent[target])
    return parent[target]

def union(parent, a, b):
    a=parent_find(parent, a)
    b=parent_find(parent, b)

    if a < b:
        parent[b]=a
    else:
        parent[a]=b

for _ in range(t):
    n=int(input())
    print(f'Scenario {_+1}:')
    parent=[i for i in range(n+1)]
    m=int(input())
    for __ in range(m):
        a, b = map(int, input().split())
        union(parent,a,b)
    # 정화
    for i in range(1, n):
        parent_find(parent, i)
    
    k=int(input())
    for ___ in range(k):
        a, b = map(int, input().split())
        if parent[a] != parent[b]:
            print(0)
        else:
            print(1)
    print()
