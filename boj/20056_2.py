import sys
import math
length, number_fire, move_order = map(int, input().split())


# k번
# 1000

# 2500000

# 모두 해도 2백만의 경우라서 상관 없을 듯.
dir_dict={
    7: (-1, -1),
    0: (-1, 0),
    1: (-1, 1),
    
    2: (0, 1),
    6: (0, -1),

    5: (1, -1),
    4: (1, 0),
    3: (1, 1),
}

def chart_maker():
    temp_chart=dict()
    global length
    for i in range(length):
        for j in range(length):
            temp_chart[(i,j)]=list()
    return temp_chart

chart=chart_maker()
new_chart=chart_maker()

# 불은 무게, 속력, 방향으로 되어있음

for i in range(number_fire):
    r, c, m, s, d=map(int, sys.stdin.readline().split())
    chart[(r-1, c-1)].append([m, s, d])

def cal_future(start_row, start_col):
    global new_chart, length, dir_dict, chart
    
    for m, s, d in chart[(start_row,start_col)]:
        dir_row, dir_col = dir_dict[d]
        new_row=(start_row + dir_row * s + length) % length
        new_col=(start_col + dir_col * s + length) % length
        new_chart[(new_row, new_col)].append((m, s, d))

def dump_chart():
    print()
    global length
    for i in range(length):
        for j in range(length):
            print(f"{i} {j}: {chart[(i, j)]}", end=' ')
        print()

def all_same(dirs):
    start=dirs[0]

    for d in dirs:
        if d != start:
            return False
    return True

def cal_merge(start_row, start_col):
    global chart, new_chart, length

    next_mass = sum([m for m, s, d in chart[(start_row, start_col)]]) // 5
    next_spd = sum([s for m, s, d in chart[(start_row, start_col)]]) // len(chart[(start_row, start_col)])
    dirs = [d % 2 for m, s, d in chart[(start_row, start_col)]]

    if next_mass == 0:
        return

    if all_same(dirs):
        for d in [0, 2, 4, 6]:
            new_chart[(start_row, start_col)].append((next_mass, next_spd, d))
    else:
        for d in [1, 3, 5, 7]:
            new_chart[(start_row, start_col)].append((next_mass, next_spd, d))

cnt=0
while cnt<move_order:
    # 새로운 chart를 생성
    new_chart=chart_maker()

    # 기존 chart를 탐색하면서 새로운 chart에 공 이동
    for i in range(length):
        for j in range(length):
            if chart[(i, j)]:
                cal_future(i, j)
    chart=new_chart
    #dump_chart()

    new_chart=chart_maker()
    
    # 새로운 chart를 이동하면서 겹치는 곳이 있다면 새롭게 계산
    for i in range(length):
        for j in range(length):
            if len(chart[(i, j)]) >= 2:
                cal_merge(i, j)
            else:
                new_chart[(i, j)] = chart[(i, j)]
    chart=new_chart
    cnt+=1

ans=0

for i in range(length):
    for j in range(length):
        ans+=sum([m for m, s, d in chart[(i,j)]])

print(ans)