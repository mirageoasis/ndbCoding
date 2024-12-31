from itertools import product
from copy import deepcopy

n=int(input())

chart=[]
new_chart=[]

for i in range(n):
    chart.append(list(map(int, input().split())))


def dump():
    global new_chart
    print()
    for c in new_chart:
        print(c)

# up
# down
# left
# right

# col 방향에서 수를 발견하는 함수
def find_col(row_num, start_col, dir):
    global new_chart, n
    while 0 <= start_col < n:
        if new_chart[row_num][start_col]:
            return start_col
        start_col+=dir
    return -1

# col에서 병합을 수행하는 함수
def cal_col(row_num, dir, start_col):
    global new_chart, n
    while True:
        # 자신 외에 0이 아닌 값을 찾는다.
        # 없으면 break
        next_idx=find_col(row_num, start_col+dir, dir)
        if next_idx == -1:
            break

        if new_chart[row_num][start_col] == 0:
            new_chart[row_num][start_col]=new_chart[row_num][next_idx]
            new_chart[row_num][next_idx]=0
        else:
            if new_chart[row_num][start_col] == new_chart[row_num][next_idx]:
                # 자신과 같음
                new_chart[row_num][start_col]*=2
                new_chart[row_num][next_idx]=0
            else:
                # 자신과 같지 않음. 자신의 진행 방향 바로 앞에 수를 놓아준다.
                temp=new_chart[row_num][next_idx]
                new_chart[row_num][next_idx]=0
                new_chart[row_num][start_col+dir]=temp
            start_col+=dir

def left():
    global new_chart, n
    for i in range(n):
        cal_col(i, 1, 0)

def right():
    global new_chart, n
    for i in range(n):
        cal_col(i, -1, n-1)

def find_row(col_num, start_row, dir):
    global new_chart, n
    while 0<=start_row<n:
        if new_chart[start_row][col_num]:
            return start_row
        start_row+=dir
    return -1

# row 
def row_col(col_num, dir, start_row):
    global new_chart, n
    while True:
        # 자신 외에 0이 아닌 값을 찾는다.
        # 없으면 break
        next_idx=find_row(col_num, start_row+dir, dir)
        if next_idx == -1:
            break
        if new_chart[start_row][col_num] == 0:
            new_chart[start_row][col_num]=new_chart[next_idx][col_num]
            new_chart[next_idx][col_num]=0
        else:
            if new_chart[start_row][col_num] == new_chart[next_idx][col_num]:
                new_chart[start_row][col_num]*=2
                new_chart[next_idx][col_num]=0
            else:
                temp=new_chart[next_idx][col_num]
                new_chart[next_idx][col_num]=0
                new_chart[start_row+dir][col_num]=temp
            start_row+=dir

def up():
    global new_chart, n
    for i in range(n):
        row_col(i, 1, 0)

def down():
    global new_chart, n
    for i in range(n):
        row_col(i, -1, n-1)


ans=0
# for move in product([1, 2, 3, 4], repeat=5):
#     #print(move)
#     new_chart=deepcopy(chart)

#     for i in range(5):
#         if move[i] == 1:
#             left()
#         elif move[i] == 2:
#             right()
#             pass
#         elif move[i] == 3:
#             up()
#             pass
#         elif move[i] == 4:
#             down()
#             pass

#     # 최대값 구하기
#     for i in range(n):
#         for j in range(n):
#             ans=max(ans, new_chart[i][j])

# print(ans)
# dump()

new_chart=deepcopy(chart)
left()
dump()
right()
right()

dump()