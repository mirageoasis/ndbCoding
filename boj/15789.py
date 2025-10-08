import sys

n, m = map(int, input().split())
parent=[i for i in range(n+1)]

def parent_find(target):
    global parent
    if parent[target] != target:
        parent[target] = parent_find(parent[target])
    return parent[target]

def union(a, b):
    global parent
    a = parent_find(a)
    b = parent_find(b)
    if a < b:
        parent[b] = a
    elif a > b:
        parent[a] = b
    else:
        pass

for _ in range(m):
    a, b= map(int, input().split())
    union(a, b)
# ctp, h, k

c, h, k = map(int, input().split())

for i in range(1, n+1):
    parent[i] = parent_find(i)

c=parent_find(c)
h=parent_find(h)

counter=[0 for i in range(n+1)]

for i in range(1, n+1):
    counter[parent_find(i)]+=1


ans_list=[]
for i in range(1, n+1):
    ans_list.append((counter[i], i))

ans_list.sort(reverse=True)


ans=counter[c]
for val, idx in ans_list:
    if k == 0:
        break
    if idx == h or idx ==c:
        continue
    ans+=val
    k-=1

print(ans)