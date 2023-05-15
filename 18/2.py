g = int(input())
p = int(input())

def parent_find(parent, t):
    if parent[t] != t:
        parent[t] = parent_find(parent, parent[t])
    return parent[t]

def union(a, b, parent):
    a_parent = parent_find(parent, a)
    b_parent = parent_find(parent, b)

    if a_parent > b_parent:
        parent[a] = b_parent
    else:
        parent[b] = a_parent

parent = [i for i in range(g+1)]

li = []

for _ in range(p):
    li.append(int(input()))

result = 0
for gate in li:
    d = parent_find(parent, gate)
    if d == 0:
        break
    else:
        union(d, d-1, parent)
        result+=1

print(result)