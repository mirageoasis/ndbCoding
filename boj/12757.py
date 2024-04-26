import sys
from collections import OrderedDict
from bisect import bisect
from collections import deque

N, M, K = map(int, input().split())

key_val = OrderedDict()

command = []

for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    key_val[a] = b

for i in range(M):
    command.append(list(map(int, sys.stdin.readline().split())))

# 1. 이미 존재하면 무시
# 2. 유일한 key가 없으면 추가 안함
# 3. 추가할 때 마다 logn이 걸리는 heap이나 추가할 때 마다 nlogn을 통해서 정렬을 해야함
# 방법 그냥 리스트 -> 추가할 때는 상관 없음, 단 탐색에서 nlogn의 시간 복잡도를 보임(비슷한 값을 찾아야 할 때 정렬을 해서) -> out
# dict를 사용 -> 찾을 때는 비슷한 값을 찾을 때(keys를 사용해서 찾을 수 있음, 문제는 이게 너무 python dependent한 문제)

def binary_search_less(iter, val):
    start = 0
    end = len(iter) - 1
    ret = -1
    # 목표한 값 보다 작은 값 중에서 최대를 찾는 것이다.
    while start <= end:
        mid = (start+end) // 2 
        if iter[mid] >= val: 
            end = mid - 1
        else:
            ret = mid
            start = mid + 1
    return ret

def binary_search_more(iter, val):
    start = 0
    end = len(iter) - 1
    ret = -1

    while start <= end:
        mid = (start+end) // 2 
        if iter[mid] >= val: 
            ret = mid
            end = mid - 1
        else:
            start = mid + 1
    return ret

def search(key_val: dict, search_val, K):
    iter = list(key_val.keys())
    #print(iter)
    min_max = binary_search_less(iter, search_val)
    max_min = binary_search_more(iter, search_val)
    print([min_max, max_min], search_val)

    if abs(min_max - search_val) > abs(max_min - search_val):
        if abs(max_min - search_val) < K:
            return [max_min]
        return []
    elif abs(min_max - search_val) < abs(max_min - search_val):
        if abs(min_max - search_val) < K:
            return [min_max]
        return []
    else:
        if abs(max_min - search_val) < K:
            return [min_max, max_min]
        return []


for c in command:
    t = c[0]

    if t == 1 and len(c) == 3:
        key_val[c[1]] = c[2]
    elif t == 2 and len(c) == 3:
        keys = search(key_val, c[1], K)
        for key in keys:
            key_val[key] = c[2]
    elif t == 3:
        keys = search(key_val, c[1], K)
        for k in keys:
            print(keys, key_val[k])
        if len(keys) == 2:
            print("?")
        elif len(keys) == 1:
            print(key_val[keys[0]])
        else:
            print(-1)

"""
5 3 5
1 10
5 20
9 30
15 40
50 50
"""
