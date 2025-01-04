import sys
n,m,q=map(int, input().split())
li=map(int, input().split())
# parent
# water dict
# 0번 제외!
parent=[i for i in range(n)]
# 앞에 청정수, 뒤에 총 count
water=[(0, 1) for i in range(n)]

for idx, val in enumerate(li):
    water[idx]=(val,1)
#print(water)
def parent_find(x):
    global parent
    if x != parent[x]:
        parent[x]=parent_find(parent[x])
    return parent[x]

def union(a, b):
    global parent
    a=parent_find(a)
    b=parent_find(b)

    if a < b:
        parent[b]=a
        water[a] = (water[a][0]+water[b][0],water[a][1]+water[b][1])
        water[b] = (0, 0)
    elif b < a:
        parent[a]=b
        water[b] = (water[a][0]+water[b][0],water[a][1]+water[b][1])
        water[a] = (0, 0)
    else:
        pass

for i in range(m):
    first, second = map(int, sys.stdin.readline().split())
    union(first-1, second-1)

for i in range(n):
    parent_find(i)
#print(water)
#print(parent)
for _ in range(q):
    num=int(sys.stdin.readline())
    clean, total = water[parent_find(num-1)]
    print(1 if clean * 2 > total else 0)