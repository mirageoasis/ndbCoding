import sys
total_cnt, m = map(int, input().split())

parent=[i for i in range(total_cnt+1)]
ans=0

def parent_find(target):
    global parent
    if parent[target] != target:
        parent[target]=parent_find(parent[target])
    return parent[target]

def union(a, b):
    global ans
    a=parent_find(a)
    b=parent_find(b)

    if a > b:
        parent[a]=b
    elif a < b:
        parent[b]=a
    else:
        ans+=1

for i in range(m):
    f, s = map(int, sys.stdin.readline().split())
    union(f, s)

for i in range(1, total_cnt+1):
    parent_find(i)

s=set()
for i in range(1, total_cnt+1):
    s.add(parent[i])

print(ans+len(s)-1)