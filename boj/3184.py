#만약에 
# 52분 시작
import sys

row_len, col_len = map(int, input().split())

chart = []
visit = [[0 for i in range(col_len)] for j in range(row_len)]
count=1

for i in range(row_len):
    chart.append(list(sys.stdin.readline().strip()))

# 만약에 row col 0 있으면 -1
from collections import deque

def bfs(row_len, col_len, start_row, start_col, count, chart, visit):
    que = deque()
    que.append((start_row, start_col))
    d_r = [1, -1, 0, 0]
    d_c = [0, 0, -1, 1]

    while que:
        row, col = que.popleft()
        for i in range(4):
            new_row = row + d_r[i]
            new_col = col + d_c[i]
            if 0<=new_row<row_len and 0<=new_col<col_len and visit[new_row][new_col] == 0 and chart[new_row][new_col] != '#':
                visit[new_row][new_col]=count
                que.append((new_row, new_col))

for i in range(row_len):
    for j in range(col_len):
        if chart[i][j] != '#' and visit[i][j] == 0:
            visit[i][j]=count
            bfs(row_len, col_len, i, j, count, chart, visit)
            count+=1


erase_set = set()
for i in range(row_len):
    for j in range(col_len):
        if i == 0 or j == 0 or i == row_len - 1 or j == col_len - 1:
            if visit[i][j] != 0:
                erase_set.add(visit[i][j])
for i in range(row_len):
    for j in range(col_len):
        if visit[i][j] in erase_set:
            visit[i][j] = -1

cal_set = set(range(1, count))
cal_set -= erase_set
cal_dict = {k:[0, 0] for k in cal_set}
# 0은 양, 1은 늑대

for i in range(row_len):
    for j in range(col_len):
        if visit[i][j] > 0:
            if chart[i][j] == 'o':
                cal_dict[visit[i][j]][0]+=1
            elif chart[i][j] == 'v':
                cal_dict[visit[i][j]][1]+=1

sheep_cnt=0
wolf_cnt=0

for _, v in cal_dict.items():
    sheep = v[0]
    wolf = v[1]

    if wolf >= sheep:
        wolf_cnt+=wolf
    else:
        sheep_cnt+=sheep

print(sheep_cnt, wolf_cnt)