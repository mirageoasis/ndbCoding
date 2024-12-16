# 16시 29분

# 정점 개수를 생각하면 플로이드 와샬하면 작살남
# disjoint set을 사용하는게?
from collections import Counter
import sys

n, m, k = map(int, input().split())

parent=[i for i in range(n+1)]

def parent_find(a):
    global parent
    if parent[a] != a:
        parent[a]=parent_find(parent[a])
    return parent[a]

def union(a, b):
    global parent
    a=parent_find(a)
    b=parent_find(b)

    if a < b:
        parent[b]=a
    else:
        parent[a]=b

for i in range(1, m+1):
    a, b = map(int, sys.stdin.readline().split())
    if i == k:
        continue
    
    union(a, b)
    #print(parent)

for i in range(1, n+1):
    parent_find(i)

c = Counter(parent[1:])
#print(c)
if len(c) == 1:
    print(0)
else:
    ans=1

    for c_1 in c.values():
        ans*=c_1
    print(ans)