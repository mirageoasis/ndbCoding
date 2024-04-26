# N 물탱크
# K 여기 방문
# M 개의 파이프
import sys


def parent_find(target, parent):
    if parent[target] != target:
        parent[target] = parent_find(parent[target], parent)
    return parent[target]

def union(first, second, parent, chart):
    a = parent_find(first, parent)
    b = parent_find(second, parent)
    if a < b:
        parent[b] = a
        chart[a] += chart[b]
        chart[b] = 0
    elif a > b:
        parent[a] = b
        chart[b] += chart[a]
        chart[a] = 0

N, K, Q = map(int, input().split())

chart = list(map(int, input().split()))
chart = [0] + chart

for i in range(len(chart)):
    if chart[i] == 0:
        chart[i] = -1

parent = [i for i in range(N+1)]

visit_list = []

for k in range(K):
    start, end = map(int, sys.stdin.readline().split())
    union(start, end, parent, chart)
    #print(parent)
    #print(chart)
    # union_find

# 방문할 물탱크의 번호
for k in range(Q):
    visit_list.append(int(sys.stdin.readline()))

for v in visit_list:
    if chart[parent_find(v, parent)] > 0:
        print(1)
    else:
        print(0)