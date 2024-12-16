import sys
n=int(input())

LIM=1000001

parent=[i for i in range(LIM+1)]
info=[1 for i in range(LIM+1)]


def parent_find(target):
    global parent
    if parent[target] != target:
        parent[target] = parent_find(parent[target])
    return parent[target]

def union(a, b):
    global parent, info
    a=parent_find(a)
    b=parent_find(b)

    if a < b:
        parent[b]=a
        info[a] += info[b]
        info[b] = 0
    elif b < a:
        parent[a]=b
        info[b] += info[a]
        info[a] = 0

for _ in range(n):
    commands = sys.stdin.readline().strip().split() 

    if commands[0] == 'I':
        union(int(commands[1]), int(commands[2]))
        #print(info[1], info[2], info[3], info[4])
    else:
        #print(f"number: {commands[1]} parent: {parent_find(int(commands[1]))} info: {info[parent_find(int(commands[1]))]}")
        print(info[parent_find(int(commands[1]))])