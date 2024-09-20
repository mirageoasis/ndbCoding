from collections import Counter, deque
from itertools import chain

row_len, col_len = map(int, input().split())

chart=[]

for i in range(row_len):
    chart.append(list(map(int, input().split())))

def dump_chart():
    for i in chart:
        print(i)

def bfs(start_row, start_col, now_idx):
    global row_len, col_len
    que = deque()
    que.append((start_row, start_col))

    d_r=[1, -1, 0, 0]
    d_c=[0, 0, 1, -1]

    while que:
        now_row, now_col = que.popleft()

        for i in range(4):
            new_row=now_row+d_r[i]
            new_col=now_col+d_c[i]

            if 0 <= new_row < row_len and 0 <= new_col < col_len and chart[new_row][new_col] == 1:
                que.append((new_row, new_col))
                chart[new_row][new_col]=now_idx
now_idx=2

for i in range(row_len):
    for j in range(col_len):
        if chart[i][j] == 1:
            chart[i][j]=now_idx
            bfs(i, j, now_idx)
            now_idx+=1


#dump_chart()

cnt = Counter(list(chain(*chart)))
if 0 in cnt:
    cnt.pop(0)

print(len(cnt.keys()))
if len(cnt.keys()):
    print(max(cnt.values()))
else:
    print(0)