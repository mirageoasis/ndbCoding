import sys

N, M = map(int, input().split())
chart = []
for i in range(M):
    chart.append(tuple(map(int, sys.stdin.readline().split())))

graph = [set() for i in range(N+1)]
travel_graph = [set() for i in range(N+1)]
# min max로 이루어짐
friend_set = set()

for start, end in chart:
    graph[start].add(end)
    graph[end].add(start)
    friend_set.add((min(start, end), max(start, end)))

ans=0

from copy import deepcopy
from itertools import chain

def find(start, graph, friend_set):    
    prev_set = deepcopy(graph[start])
    
    new_friend = set(chain(*[list(graph[i]) for i in graph[start]]))
    new_friend.remove(start)

    return prev_set | new_friend
    # for n in temp:
    #     friend_set.add((min(n, start), max(n, start)))
ans_list = []
while len(friend_set) < (N * (N - 1)) // 2:
    prev_cnt = len(friend_set)
    #print(friend_set)
    #print(prev_cnt)
    new_graph = [set() for i in range(N+1)]
    # 과정
    for i in range(1, N+1):
        new_graph[i] = find(i, graph, friend_set)
    
    for i in range(1, N+1):
        temp_set = new_graph[i]
        for t in temp_set:
            friend_set.add((min(i, t), max(i, t)))

    graph = new_graph
    #print(friend_set)
    #print(len(friend_set))
    ans_list.append(len(friend_set) - prev_cnt)
    ans+=1

print(ans)
for a in ans_list:
    print(a)