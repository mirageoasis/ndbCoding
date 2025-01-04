import sys
from collections import deque

row_len, col_len = map(int,  input().split())
chart=[]
visit=[[False for i in range(col_len)] for j in range(row_len)]

for _ in range(row_len):
    chart.append(list(map(int, sys.stdin.readline().split())))

def dump():
    for c in chart:
        print(c)

ans=0
def dfs(start_row, start_col, idx, summ):
    global row_len, col_len, chart, visit, ans

    if idx == 3:
        ans=max(ans, summ)
        return

    d_r=[1, -1, 0, 0]
    d_c=[0, 0, 1, -1]
    for i in range(4):
        new_row=start_row+d_r[i]
        new_col=start_col+d_c[i]

        if 0<=new_row<row_len and 0<=new_col<col_len and not visit[new_row][new_col]:
            visit[new_row][new_col]=True
            dfs(new_row, new_col, idx+1, summ+chart[new_row][new_col])
            visit[new_row][new_col]=False


for i in range(row_len):
    for j in range(col_len):
        visit[i][j]=True
        dfs(i, j, 0, chart[i][j])
        visit[i][j]=False

for row in range(row_len):
    for col in range(col_len):
        # 여기에서 따로 계산
        d_r=[1, -1, 0, 0]
        d_c=[0, 0, 1, -1]
        temp_summ=chart[row][col]
        for i in range(4):
            new_row=row+d_r[i]
            new_col=col+d_c[i]
            if 0<=new_row<row_len and 0<=new_col<col_len:
                temp_summ+=chart[new_row][new_col]
        
        for i in range(4):
            new_row=row+d_r[i]
            new_col=col+d_c[i]
            if 0<=new_row<row_len and 0<=new_col<col_len:
                ans=max(ans, temp_summ - chart[new_row][new_col])
            else:
                ans=max(ans, temp_summ)
print(ans)