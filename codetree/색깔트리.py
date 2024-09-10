# 부모
# 색깔
# 깊이 -> 위에서 탐색하면서 최소 저장
# 루트 노드

# 삽입 연산
# 이 때 부모 타고 올라가서 자신이 속해있다는 사실 공표해야 시간 복잡도 아낄 듯

# 색깔 변경

# 색깔 조회

# 점수 조회
# 가치 계산은 재귀함수로

# 탐색 연산
# log e + v => 20000 노드 + 10000

import sys
from collections import deque, defaultdict

N=int(input())

commands=[]

for i in range(N):
    commands.append(list(map(int, sys.stdin.readline().split())))

#자신의 모든 자식을(손자까지) 남겨주는 dictionary
child = defaultdict(list)

# 정보를 저장하는 dictionary
info_dict = dict()

# 루트 목록 저장
root_info = set()

# 색깔 임시 계산
temp_color_dict=defaultdict(set)

def add_root(c):
    info_dict[c[1]]=[c[2], c[3], c[4], c[1]]
    root_info.add(c[1])

def add_node(c):
    # 성공하면 info_dict
    # 성공하면 near_child
    _, my_id, parent_id, color, my_depth = c

    parent_parent_id, parent_color, parent_depth, parent_root_id = info_dict[parent_id]

    if parent_depth == 1 or parent_depth == 0:
        return
    
    max_depth = min(my_depth, parent_depth-1)

    info_dict[my_id] = [parent_id, color, max_depth, parent_root_id]
    
    # 모든 자식들 추가
    while parent_id != -1:
        child[parent_id].append(my_id)
        
        parent_id, _, a, b = info_dict[parent_id]


def change(command):
    _, my_id, color = command
    #자신 색깔
    info_dict[my_id][1] = color
    #자식 색깔
    for i in child[my_id]:
        info_dict[i][1] = color


def value():
    temp_color_dict = defaultdict(set)
    
    for i in info_dict:
        # 내 색깔
        temp_color_dict[i].add(info_dict[i][1])
        # 자식의 색깔 추출
        for j in child[i]:
            temp_color_dict[i].add(info_dict[j][1])

    #print(child)
    #print(temp_color_dict)
    return sum([len(i) ** 2 for i in temp_color_dict.values()])



for command in commands:
    c = command[0]

    if c == 100:
        if command[2] == -1:
            add_root(command)
        else:
            add_node(command)
        #print(child)
    elif c == 200:
        change(command)
    elif c == 300:
        print(f"{info_dict[command[1]][1]}")
    elif c== 400:
        print(value())

#print(info_dict)
#print(root_info)
#print(near_child)