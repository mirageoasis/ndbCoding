import sys

n, m = map(int, input().split())

# bfs도 되긴하는데
# 그냥 disjoint set으로

li=[]
parent=[i for i in range(n+1)]

def union(a, b):
    a=parent_find(a)
    b=parent_find(b)

    if a < b:
        parent[b] = a
    elif b < a:
        parent[a] = b

def parent_find(target):
    global parent
    if parent[target] != target:
        parent[target] = parent_find(parent[target])
    return parent[target]

for i in range(m):
    st, ed = map(int, sys.stdin.readline().split())

    union(st, ed)
    #print(parent)

for i in range(1, n+1):
    parent_find(i)
#print(parent)
print(sum([1 for idx, val in enumerate(parent) if idx == val]) - 1)