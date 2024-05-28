# 2분 시작
import sys
chart = []
minus_chart = []
row_len, col_len = map(int, input().split())

for i in range(row_len):
    chart.append(list(map(int, sys.stdin.readline().split())))

visit = [[False for i in range(col_len)] for j in range(row_len)]

# 90000 * 

from collections import deque

def counter(row, col):
    d_r = [0, 0, -1, 1]
    d_c = [1, -1, 0, 0]
    ret=0
    for i in range(4):
        new_row = row + d_r[i]
        new_col = col + d_c[i]
        if 0<=new_row<row_len and 0<=new_col<col_len and chart[new_row][new_col] == 0:
            ret+=1
    return ret

def bfs(start_row, start_col):
    que = deque()
    que.append((start_row, start_col))
    minus_chart[start_row][start_col] = counter(start_row, start_col)

    d_r = [0, 0, -1, 1]
    d_c = [1, -1, 0, 0]

    while que:
        row, col = que.popleft()

        for i in range(4):
            new_row = row + d_r[i]
            new_col = col + d_c[i]

            if 0<=new_row<row_len and 0<=new_col<col_len and not visit[new_row][new_col] and chart[new_row][new_col]:
                visit[new_row][new_col]=True
                minus_chart[new_row][new_col] = counter(new_row, new_col)
                que.append((new_row, new_col))

ans=0
while True:
    visit=[[False for i in range(col_len)] for j in range(row_len)]
    minus_chart=[[0 for i in range(col_len)] for j in range(row_len)]
    temp_tick=0
    for i in range(row_len):
        for j in range(col_len):
            if chart[i][j] != 0 and not visit[i][j]:
                if temp_tick == 0:
                    bfs(i, j)
                temp_tick+=1
    
    for i in range(row_len):
        for j in range(col_len):
            chart[i][j]-=minus_chart[i][j]
            chart[i][j] = max(chart[i][j], 0)

    # print('---')
    # for c in chart:
    #     print(c)
    # print('---')

    if temp_tick > 1:
        print(ans)
        break
    if temp_tick == 0:
        print(0)
        break
    ans+=1
