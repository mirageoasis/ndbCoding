import sys
input=sys.stdin.readline

n, m, k = map(int, input().split())

pay=list(map(int, input().split()))
pay.insert(0, 0)
parent=[i for i in range(n+1)]

def parent_find(x):
    global parent
    if parent[x] != x:
        parent[x] = parent_find(parent[x])
    return parent[x]

def union(a, b):
    global pay, parent
    a=parent_find(a)
    b=parent_find(b)

    if a!=b:
        if pay[a] < pay[b]:
            parent[b]=a
        else:
            parent[a]=b


# 최소를 구하고 안되면 gg
for i in range(m):
    a, b = map(int, input().split())
    union(a, b)

# 정화
for i in range(1, n+1):
    parent_find(i)

s=set()
for i in range(1, n+1):
    s.add(parent_find(i))

lim=sum([pay[a] for a in s])

if lim > k:
    print("Oh no")
else:
    print(lim)
