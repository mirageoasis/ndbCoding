# 8시 49분 시작

# 상하좌우중 1칸

# 사라진 기사 아무반응 x

# 충돌 판정 어떻게 낼 것인가?
# 다 통과되면 함정 파악

# dict로 기사 칸 저장.
import sys
from collections import deque

size, knight_numbers, order_number = map(int, sys.stdin.readline().split())
#[칸], 처음 체력, 지금 체력
knight_dict = dict()
chart=[]
orders=[]
direction_chart=[(-1, 0), (0, 1), (1, 0), (0, -1)]
import copy

def dump_chart():
    # 함정과 knight 있으면 x표시 한다.
    print_chart = copy.deepcopy(chart)
    for k, v in knight_dict.items():
        chan, ori_health, now_health = v
        if now_health <= 0:
            continue

        for r, c in chan:
            if print_chart[r][c] == 1:
                print_chart[r][c] = f"-x{k}"
            else:
                print_chart[r][c]=-k
    
    print()
    for i in range(size):
        for j in range(size):
            print("%4s"%(str(print_chart[i][j])), end=' ')
        print()
    
    print()

for i in range(size):
    chart.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, knight_numbers+1):
    # 행, 렬, 높이, 넓이, 체력
    row, col, height, width, health = map(int, sys.stdin.readline().split())
    row-=1
    col-=1
    knight_loc=[]
    for j in range(height):
        for k in range(width):
            knight_loc.append((row+j, col+k))
    knight_dict[i] = [knight_loc, health, health]

for i in range(order_number):
    orders.append(list(map(int, sys.stdin.readline().split())))

#print(knight_dict)
#dump_chart()

# 
# 기사 번호, 움직이는 방향
def move(knight_number, direction, origin_knight):
    chans, ori_health, now_health = knight_dict[knight_number]
    new_chans=[]
    for row, col in chans:
        new_row=row+direction_chart[direction][0]
        new_col=col+direction_chart[direction][1]
        if chart[new_row][new_col] == 1 and knight_number != origin_knight:
            now_health-=1
        new_chans.append((new_row, new_col))
    knight_dict[knight_number] = [new_chans, ori_health, now_health]

def moveable(row, col):
    if row < 0:
        return False
    if row >= size:
        return False
    if col < 0:
        return False
    if col >= size:
        return False
    if chart[row][col]==2:
        return False
    return True

def moveable_knight(knight_number, direction):
    # 벽 있거나
    # 범위 벗어났거나
    chans, a, b = knight_dict[knight_number]
    mov_row, mov_col=direction_chart[direction]
    for row, col in chans:
        new_row=row+mov_row
        new_col=col+mov_col
        if not moveable(new_row, new_col):
            return False
    
    return True

def cal_chans():
    ret=dict()
    
    for k, v in knight_dict.items():
        chans, a, b = v
        for row, col in chans:
            ret[(row, col)] = k
    return ret

#dump_chart()

for now_key, direction in orders:
    #print()
    # 기사가 없다면 skip
    if now_key not in knight_dict:
        continue

    # 기사들의 모든 위치가 나와있다.
    current_loc=cal_chans()
    #print(f"current loc: {current_loc}")
    visit=set()
    mov_row, mov_col = direction_chart[direction]
    wall_flag = False
    
    # 일단 지금 기사를 queue에 넣어준다.
    # 그리고 current_loc에 해당하는 (row, col)이 있다면 해당 기사도 넣어준다.
    # visit이라는 set을 만들어서 해당 기사가 이미 들어가 있다면 무효
    # 기사가 없을 때 까지 que를 돌린다.
    
    que=deque()
    que.append(now_key)
    visit.add(now_key)

    while que:
        # 기사 번호 추출
        knight_number=que.popleft()
        #print(f"knight number {knight_number}")
        chans, a, b = knight_dict[knight_number]
        for row, col in chans:
            new_row=row+mov_row
            new_col=col+mov_col
            #print(new_row, new_col)
            new_chan=(new_row, new_col)
            if new_chan in current_loc:
                new_number = current_loc[new_chan]
                if new_number not in visit:
                    visit.add(new_number)
                    que.append(new_number)
        #print(f"visit temp: {visit}")

    #print(f"visit: {visit}")

    # 움직일 기사들 set로 기사들 미리 움직여보기
    for knight_number in visit:
        if not moveable_knight(knight_number, direction):
            wall_flag=True

    #만약에 못 움직이면 wall_flag를 무효처리
    if wall_flag:
        #print("failed")
        continue
    
    # visit set를 탐색하면서 옮겨야할 기사들 다 옮긴다.
    for knight_number in visit:
        move(knight_number, direction, now_key)

    # 모두 체력 깎기, 체력 0인 기사들 퇴출 
    for knight_number in visit:
        if knight_dict[knight_number][2] <= 0:
            knight_dict.pop(knight_number)

    #dump_chart()
    #print(knight_dict)

ans=0
for knight in knight_dict:
    a, ori_health, now_health=knight_dict[knight]
    ans+=(ori_health-now_health)
#print(knight_dict)

print(ans)


"""
4 3 3
0 0 1 0
0 0 1 0
1 1 0 1
0 0 2 0
1 2 2 1 5
2 1 2 1 1
3 2 1 2 3
1 2
2 1
3 3

4 3 3
0 0 1 0
0 0 1 0
1 1 0 1
0 0 2 0
1 2 2 1 5
2 1 2 1 1
3 2 1 2 3
1 2
2 1
3 3

4 3 3
0 0 1 0
0 0 1 0
1 1 0 1
0 0 0 0
2 4 2 1 5
2 2 2 1 5
3 3 2 1 3
1 3
3 3
2 1
"""
