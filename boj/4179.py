from collections import deque
import sys

# 47분 

row_len, col_len = map(int, input().split())
chart=[]
j_visit=[[False for i in range(col_len)] for j in range(row_len)]
f_visit=[[False for i in range(col_len)] for j in range(row_len)]

for i in range(row_len):
    chart.append(list(sys.stdin.readline().strip()))

# for c in chart:
#     print(c)

# row, col, time
j_que=deque()
# row, col
f_que=deque()


def bfs(j_que, f_que):
    global row_len, col_len
    d_r=[-1, 1, 0, 0]
    d_c=[0, 0, -1, 1]



    while j_que:
        # j_que 실행
        temp_j_que=deque()
        while j_que:
            #print(j_que)
            now_row, now_col, time = j_que.popleft()
            if f_visit[now_row][now_col]:
                continue

            if (now_row == row_len - 1) or (now_row == 0) or (now_col == col_len - 1) or (now_col == 0):
                #print(now_row, now_col)
                return time

            for i in range(4):
                new_row = now_row + d_r[i]
                new_col = now_col + d_c[i]

                if 0<=new_row<row_len and 0<=new_col<col_len and not j_visit[new_row][new_col] and not f_visit[new_row][new_col] and chart[new_row][new_col] != '#':
                    j_visit[new_row][new_col]=True
                    temp_j_que.append((new_row, new_col, time+1))
        j_que=temp_j_que

        temp_f_que=deque()
        while f_que:
            now_row, now_col = f_que.popleft()
            for i in range(4):
                new_row = now_row + d_r[i]
                new_col = now_col + d_c[i]

                if 0<=new_row<row_len and 0<=new_col<col_len and not f_visit[new_row][new_col] and chart[new_row][new_col] != '#':
                    f_visit[new_row][new_col]=True
                    temp_f_que.append((new_row, new_col))
        f_que=temp_f_que

    return -1


for i in range(row_len):
    for j in range(col_len):
        if chart[i][j] == 'J':
            j_que.append((i, j, 1))
            j_visit[i][j]=True
        if chart[i][j] == 'F':
            f_que.append((i, j))
            f_visit[i][j]=True
ans=bfs(j_que, f_que)

if ans == -1:
    print("IMPOSSIBLE")
else:
    print(ans)
