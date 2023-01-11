
'''
union find 는 2가지 연산을 요구한다. 
1. parent 찾는 연산
2. union을 하는 연산

-> union을 할 때 parent find연산을 진행해야 한다. 이 때 번호가 작은 쪽으로 parent를 지정하는 것이다.

문제는 parent를 찾는 연산이 너무 빈번하게 일어나면 시간 복잡도 문제가 발생 할 수 있으므로 
parent를 정리하는 연산또한 필요하다.


'''

N = int(input())
parent_list = [0] * N

def find_parent(parent_list, n):
    if parent_list[n] != n:
        return find_parent(parent_list, parent_list[n])
    return n

def compression_find_parent(parent_list, n):
    if n != parent_list[n]:
        parent_list[n] = compression_find_parent(parent_list, n)
    return parent_list[n]



def union(a, b, parent_list):
    a_p = parent_list[a]
    b_p = parent_list[b]

    # 최상위 노드의 부모가 바뀌도록 유도
    if a_p < b_p:
        parent_list[b_p] = a_p
    else:
        parent_list[a_p] = b_p