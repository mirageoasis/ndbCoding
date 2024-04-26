import sys 

N=int(input())

parent = [i for i in range(N+1)]

def parent_find(first):
    global parent
    if parent[first] != first:
        parent[first] = parent_find(parent[first])
    return parent[first]

def union(first, second):
    first_p = parent_find(first)
    second_p = parent_find(second)

    if first_p < second_p:
        parent[second_p] = first_p
    else:
        parent[first_p] = second_p


for i in range(N-2):
    first, second = map(int, sys.stdin.readline().split())
    union(first, second)

for i in range(1, N+1):
    parent_find(i)

#print(parent[1:])

print(*list(set(parent[1:])))