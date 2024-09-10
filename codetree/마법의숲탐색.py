# 20분 시작

# 1행
# R행
# -> 행 1씩 다 뺀다.

# ci 열

# 남쪽으로 내려간다.
# 출구가 골렘과 인접하면 다른 골렘으로
# 만약에 못 움직이면 비워진다.

from collections import deque
import sys

row_len, col_len, fairy_num = map(int, sys.stdin.readline().split())

chart = [[0 for i in range(col_len)] for j in range(row_len+3)]

def clean_chart():
    global chart
    chart = [[0 for i in range(col_len)] for j in range(row_len+3)]

def dump_chart():
    global chart
    
    for c in chart:
        print(c)


def moveable_part(row, col):
    if row > row_len + 2:
        return False
    if col < 0:
        return False
    if col >= col_len:
        return False
    if chart[row][col] != 0:
        return False
    return True

def moveable(row, col):
    global chart
    # main
    # north
    # west
    # east
    # south
    return moveable_part(row, col) \
        and moveable_part(row-1, col) \
        and moveable_part(row, col-1) \
        and moveable_part(row, col+1) \
        and moveable_part(row+1, col)

def bfs(row, col, visit):
    que=deque()
    que.append((row, col))
    visit[row][col]=True
    ret=2
    dr=[1, -1, 0, 0]
    dc=[0, 0, -1, 1]
    #print(f"start {row} {col}")
    while que:
        now_row, now_col = que.popleft()
        if ret < now_row:
            ret=now_row
            #print(f"maxi {now_row} {now_col}")

        for i in range(4):
            new_row=now_row+dr[i]
            new_col=now_col+dc[i]
            if new_row > row_len + 2:
                continue
            if new_col < 0:
                continue
            if new_col >= col_len:
                continue
            if visit[new_row][new_col]:
                continue
            if chart[new_row][new_col] == 0:
                continue
            if chart[now_row][now_col] < 0:
                que.append((new_row, new_col))
                visit[new_row][new_col]=True
            
            if chart[now_row][now_col] > 0 and abs(chart[now_row][now_col]) == abs(chart[new_row][new_col]):
                que.append((new_row, new_col))
                visit[new_row][new_col]=True


    return ret-2


dir_cal=[(-1,0), (0,1), (1,0), (0,-1)]

ans=0

for i in range(1, fairy_num+1):
    # 숫자 0,1,2,3 북, 동, 남, 서
    # 서쪽으로 가면 +1 해준다.
    col, exit_dir = map(int, sys.stdin.readline().split())
    # 항상 빼줘야 한다.
    col-=1

    # 1에서 시작
    now_row, now_col = 1, col
    while True:
        # south로 간 경우
        # 안되면 서쪽으로 이동한 다음 남쪽 본다.
        # 안되면 동쪽으로 이동한 다음 남쪽 본다.
        if moveable(now_row+1, now_col):
            now_row+=1
        elif moveable(now_row, now_col-1) and moveable(now_row+1, now_col-1):
            now_row+=1
            now_col-=1
            exit_dir= (4+ exit_dir -1) % 4
        elif moveable(now_row, now_col+1) and moveable(now_row+1, now_col+1):
            now_row+=1
            now_col+=1
            exit_dir = (exit_dir+1) % 4
        else:
            break

    # 만약에 현 위치가 3 이하라면 chart clear, out!
    if now_row <= 3:
        clean_chart()
        continue
    # 전부 처리
    chart[now_row-1][now_col] = i
    chart[now_row+1][now_col] = i
    chart[now_row][now_col-1] = i
    chart[now_row][now_col+1] = i
    chart[now_row][now_col] = i

    chart[now_row+dir_cal[exit_dir][0]][now_col+dir_cal[exit_dir][1]]*=-1

    # 이제 bfs
    visit=[[False for i in range(col_len)] for j in range(row_len+3)]
    res = bfs(now_row, now_col, visit)
    ans+= res
    # print("res")
    # print(now_row, now_col)
    # dump_chart()
    # print(res)
    # print()

print(ans)