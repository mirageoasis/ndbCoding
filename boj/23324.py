import sys
from collections import defaultdict

N, M, K = map(int, input().split())

parent_list = [i for i in range(N + 1)]

def parent_find(a):
    if a != parent_list[a]:
        parent_list[a] = parent_find(parent_list[a])
    return parent_list[a]

def union(a, b):
    a_parent = parent_find(a)
    b_parent = parent_find(b)
    
    if a_parent > b_parent:
        parent_list[a_parent] = parent_list[b_parent]
    elif b_parent > a_parent:
        parent_list[b_parent] = parent_list[a_parent]


for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    if i != K - 1:
        union(a, b)


parent_dict = defaultdict(list)

for i in range(1, N + 1):
    parent_find(i)

for i in range(1, N + 1):
    parent_dict[parent_list[i]].append(i)

ans=0

for i in range(1, N + 1):
    ans+= N - len(parent_dict[parent_list[i]])

print(ans // 2)