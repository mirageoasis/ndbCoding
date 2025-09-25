import sys
input=sys.stdin.readline
n, m = map(int, input().split())

parent=[i for i in range(n+1)]
ans=1
# parent를 구하고 각 개수를 전부 곱해준다.

def parent_find(target):
    global parent
    if parent[target] != target:
        parent[target]=parent_find(parent[target])
    return parent[target]

for i in range(m):
    a, b = map(int, input().split())
    a=parent_find(a)
    b=parent_find(b)

    if a < b:
        parent[b]=a
    else:
        parent[a]=b

for i in range(1, n+1):
    parent_find(i)
from collections import defaultdict
ans_dict=defaultdict(int)
for i in range(1, n+1):
    ans_dict[parent[i]]+=1

for k, v in ans_dict.items():
    ans*=v
    ans%=1000000007

#print(parent)

print(ans)
