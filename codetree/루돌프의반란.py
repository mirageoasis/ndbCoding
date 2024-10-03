# 거리는 row ^ 2 + col ^ 2
# 우선순위 한칸 돌진

# 루돌프는 1개

# 가장 가까운 산타. 거리 same r이 제일 큰, 다음은 c가 제일 큰

# 산타는 상하좌우로 인접한 4방향 중 한 곳으로 움직일 수 있습니다. 이때 가장 가까워질 수 있는 방향이 여러 개라면, 상우하좌 우선순위에 맞춰 움직입니다.

# 루돌프가 충돌 산타 C, 그리고 루돌프 이동 방향으로 C칸 밀림
# 산타 움직이면 D 점, 산타는 D 만큼의 점수를 얻게 된다. 그리고 반대 방향으로 D 만큼 밀려남-> 밀려나기 시작한 점에서 부터 계산하기

# 밀려났는데 산타 있으면 상호작용
# 산타가 착지할 때 그 칸에 산타 있으면 밀려남. 그리고 거기에도 있으면 밀려남

# 루돌프와 충돌하면 기절. 

# 탈락하지 않은 산타에게 1점 부여

# 번호, 초기위치-> 1씩 제외하기
# set으로 기절한 산타 번호 기입
from collections import deque, defaultdict

chart_size, turn_nums, santa_nums, deer_pow, santa_pow = map(int, input().split())
deer_row, deer_col = map(int, input().split())
deer_row-=1 
deer_col-=1

santa_info_dict=dict()
santa_score_dict=defaultdict(int)
chart=[[0 for i in range(chart_size)] for j in range(chart_size)]

def dump_chart():
    pri=[[0 for i in range(chart_size)] for j in range(chart_size)]

    for k, v in santa_info_dict.items():
        santa_row, santa_col = v
        pri[santa_row][santa_col]=k
    
    pri[deer_row][deer_col]=9

    for i in pri:
        print(i)
    print()

for i in range(santa_nums):
    santa_num, row, col = map(int, input().split())
    santa_info_dict[santa_num]=[row-1, col-1] 

# list로 준다.
def santa_to_move(row, col):
    # 산타번호, 거리, row, col
    ret=[]

    for k, v in santa_info_dict.items():
        santa_row, santa_col = v
        ret.append([k, (santa_row - row) ** 2 + (santa_col - col) ** 2, santa_row, santa_col])
    ret.sort(key= lambda x : (x[1], -x[2], -x[3]))
    
    return ret[0]

# 거리, 이동한 row, 이동한 col
def cal_deer_dir(selected_santa, deer_row, deer_col):
    # (산타 번호,거리, row, col)
    santa_number, distance, santa_row, santa_col = selected_santa
    d_r=[1, 1, 1, -1, -1, -1, 0, 0]
    d_c=[1, 0, -1, 0, 1, -1, 1, -1]
    ret=[]
    #print(santa_number)
    for r, c in zip(d_r, d_c):
        new_row = r+deer_row
        new_col = c+deer_col
        ret.append([(santa_row - new_row) ** 2 + (santa_col - new_col) ** 2, r, c])
    ret.sort(key=lambda x: (x[0]))
    print(ret)

    return ret[0]

def move_deer(deer_move_dir):
    global deer_row, deer_col
    _, deer_move_row, deer_move_col = deer_move_dir
    deer_row+=deer_move_row
    deer_col+=deer_move_col


def santa_locs():
    ret=dict()
    for k, v in santa_info_dict.items():
        row, col = v
        ret[(row, col)] = k
    return ret

def collison_santa(santa_location_dict, deer_move_dir):
    global deer_row, deer_col, deer_pow
    # 움직인 방향
    _, mov_row, mov_col = deer_move_dir

    # 없으면 ㅂㅂ
    if (deer_row, deer_col) not in santa_location_dict:
        return
    
    # 있으면 충돌 판정 시작!
    que=deque()
    santa_idx = santa_location_dict[(deer_row, deer_col)]
    old_row, old_col = santa_info_dict[santa_idx]
    new_row, new_col = old_row+mov_row * deer_pow, old_col + mov_col * deer_pow
    santa_info_dict[santa_idx]=[new_row, new_col]
    santa_score_dict[santa_idx]+=deer_pow
    new_dizzy_santa.add(santa_idx)

    # 2차 피해
    if (new_row, new_col) not in santa_location_dict:
        return

    visit=set()
    que.append((new_row, new_col))
    visit.add(santa_location_dict[(new_row, new_col)])

    #2차 피해
    while que:
        old_row, old_col = que.popleft()
        new_row, new_col = old_row+mov_row, old_col+mov_col

        if (new_row, new_col) in santa_location_dict:
            que.append((new_row, new_col))
            visit.add(santa_location_dict[(new_row, new_col)])


    #2차 피해 입은 친구들 수정
    for santa_idx in visit:
        old_row, old_col =  santa_info_dict[santa_idx]
        new_row=old_row+mov_row
        new_col=old_col+mov_col

        santa_info_dict[santa_idx] = [new_row, new_col]

def delete_santa():
    ss=set()
    for k, v in santa_info_dict.items():
        row, col = v
        if row >= chart_size or row < 0 or col >= chart_size or col < 0:
            ss.add(k)
    
    for s in ss:
        santa_info_dict.pop(s)

def move_santa():
    d_r=[1, -1, 0, 0]
    d_c=[0, 0, -1, 1]

    
    
    pass

now_turn=0
dizzy_santa=set()
new_dizzy_santa=set()
while now_turn < turn_nums:
    

    # 움직일 산타 선택
    santa_location_dict=santa_locs()
    selected_santa = santa_to_move(deer_row, deer_col)
    deer_move_dir= cal_deer_dir(selected_santa, deer_row, deer_col)
    # 루돌프 이동
    move_deer(deer_move_dir)
    
    # 산타 충돌 판정
    collison_santa(santa_location_dict, deer_move_dir)
    print(santa_info_dict)
    # 밖으로 밀려난 산타 삭제 info로 산타 삭제
    delete_santa()

    # info 기준으로 업데이트
    santa_location_dict=santa_locs()

    # 산타 이동
    # new_dizzy나 idzzy에 있으면 움직이기 x
    for k in santa_info_dict:
        if k in new_dizzy_santa or k in dizzy_santa:
            continue
        move_santa(k, santa_location_dict)
        delete_santa()
        santa_location_dict=santa_locs()

    print(deer_move_dir)
    dump_chart()
    
    # 턴 종료후 점수 더하기
    for k in santa_info_dict:
        santa_score_dict[k]+=1

    # 마지막 동기화
    dizzy_santa=new_dizzy_santa
    now_turn+=1