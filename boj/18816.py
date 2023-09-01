import sys

N=int(input())


parent_list = [i for i in range(1000001)]
child_count_list = [1 for i in range(1000001)]

# 이거 안전하게 하려면 parent가 같으면 merge 연산을 하게 하면 안된다. 
# parent 같은 경우를 만들면 값이 2배로 뻥튀기가 된다.
def union(a, b):
    a_parent = parent_find(parent_list, a)
    b_parent = parent_find(parent_list, b)

    if a_parent < b_parent:
        parent_list[b_parent] = a_parent
        child_count_list[a_parent] += child_count_list[b_parent]
        child_count_list[b_parent] = 0
    elif a_parent > b_parent:
        parent_list[a_parent] = b_parent
        child_count_list[b_parent] += child_count_list[a_parent]
        child_count_list[a_parent] = 0


def parent_find(parent_list, target):
    if parent_list[target] != target:
        parent_list[target] = parent_find(parent_list, parent_list[target])
    return parent_list[target]


for i in range(N):
    inputs = sys.stdin.readline().split()
    
    if inputs[0] == 'Q':
        first = int(inputs[1])
        print(child_count_list[parent_find(parent_list, first)])
    else:
        first = int(inputs[1])
        second = int(inputs[2])
        union(first, second)

#print(parent_list[:10])
#print(child_count_list[:10])