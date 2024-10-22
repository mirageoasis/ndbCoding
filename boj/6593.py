# 12시 3분
from collections import deque

def dump():
    for b in build:
        for r in b:
            print(r)
        print()

def moveable(new_lvl, new_row, new_col):
    global level, row_len, col_len
    if 0<=new_lvl<level and 0 <= new_row <row_len and 0<=new_col<col_len and not visit[new_lvl][new_row][new_col] and build[new_lvl][new_row][new_col] != '#':
        return True
    
    return False

def bfs(start_level, start_row, start_col):
    global level, row_len, col_len
    que=deque()
    que.append((start_level, start_row, start_col, 0))

    d_l=[0, 0, 0, 0, 1, -1]
    d_r=[1, -1, 0, 0, 0, 0]
    d_c=[0, 0, 1, -1, 0, 0]

    while que:
        now_lvl, now_row, now_col, time = que.popleft()

        if build[now_lvl][now_row][now_col] == 'E':
            return time

        for i in range(6):
            new_lvl=now_lvl+d_l[i]
            new_row=now_row+d_r[i]
            new_col=now_col+d_c[i]

            if moveable(new_lvl, new_row, new_col):
                visit[new_lvl][new_row][new_col]=True
                que.append((new_lvl, new_row, new_col, time+1))


    return -1

while True:
    level, row_len, col_len = map(int, input().split())
    if level == 0 and row_len == 0 and col_len == 0:
        break

    build=[]
    visit=[[[False for i in range(col_len)] for j in range(row_len)] for k in range(level)]


    for i in range(level):
        t=[]
        for j in range(row_len):
            t.append(list(input()))
        build.append(t)
        input()

    start_level=0
    start_row=0
    start_col=0
    for i in range(level):
        for j in range(row_len):
            for k in range(col_len):
                if build[i][j][k] == 'S':
                    start_level=i
                    start_row=j
                    start_col=k

    res = bfs(start_level, start_row, start_col)

    if res == -1:
        print("Trapped!")
    else:
        print(f"Escaped in {res} minute(s).")