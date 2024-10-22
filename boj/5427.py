# 10시 31분 시작
import sys
from collections import deque
T=int(input())
chart=[]

def dump_chart():
    for c in chart:
        print(c)

def f_chart():
    for f in f_visit:
        print(f)

def movable(row, col):
    global row_len, col_len
    if 0<=row<row_len and 0<=col<col_len and not chart[row][col] == '#':
        return True
    return False



def bfs(s_queue, f_queue):
    global row_len, col_len
    
    d_r=[1, -1, 0, 0]
    d_c=[0, 0, -1, 1]

    while s_queue:
        temp_f_queue=deque()
        temp_s_queue=deque()

        # f_queue 추출
        while f_queue:
            now_row, now_col = f_queue.popleft()
        
            for i in range(4):
                new_row=now_row+d_r[i]
                new_col=now_col+d_c[i]
                #print(new_row, new_col)
                if movable(new_row, new_col) and not f_visit[new_row][new_col]:
                    f_visit[new_row][new_col]=True
                    temp_f_queue.append((new_row, new_col))
        # s_queue 추출
        while s_queue:
            now_row, now_col, time = s_queue.popleft()

            if now_row == 0 or now_row == row_len - 1 or now_col == 0 or now_col == col_len - 1:
                #print(now_row, now_col)
                return time

            for i in range(4):
                new_row=now_row+d_r[i]
                new_col=now_col+d_c[i]
                if movable(new_row, new_col) and not s_visit[new_row][new_col] and not f_visit[new_row][new_col]:
                    s_visit[new_row][new_col]=True
                    temp_s_queue.append((new_row, new_col, time+1))
        
        f_queue=temp_f_queue
        s_queue=temp_s_queue

    return -1

for _ in range(T):
    col_len, row_len = map(int, input().split())
    chart=[]
    for __ in range(row_len):
        chart.append(list(sys.stdin.readline().strip()))
    
    #dump_chart()
    s_visit=[[False for i in range(col_len)] for j in range(row_len)]
    f_visit=[[False for i in range(col_len)] for j in range(row_len)]
    s_queue=deque()
    f_queue=deque()
    
    for i in range(row_len):
        for j in range(col_len):
            if chart[i][j] == '*':
                f_queue.append((i, j))
                f_visit[i][j]=True

            if chart[i][j] == '@':
                s_queue.append((i, j, 1))
                s_visit[i][j]=True
    
    res = bfs(s_queue, f_queue)

    if res == -1:
        print("IMPOSSIBLE")
    else:
        print(res)
