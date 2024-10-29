# 3시 38분 시작
import sys

N, M = map(int, input().split())

parent=[i for i in range(N+1)]

def parent_find(a):
    if parent[a] != a:
        parent[a] = parent_find(parent[a])
    return parent[a]
temp=0
def union(a, b):
    global temp
    a=parent_find(a)
    b=parent_find(b)
    if a < b:
        parent[b]=a
    elif a > b:
        parent[a]=b
    else:
        # 같다면
        temp+=1


for i in range(M):
    a, b = map(int, sys.stdin.readline().split())

    union(a,b)

ans_set=set()

for i in range(1, N+1):
    parent_find(i)

for i in range(1, N+1):
    if i == parent_find(i):
        ans_set.add(i)

print(len(ans_set) - 1 + temp)