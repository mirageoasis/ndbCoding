# 40분 시작
import sys
from collections import deque, defaultdict

row_len, col_len, s_num = map(int, input().split())

# 100 100 100
chart=[[0 for i in range(col_len)] for j in range(row_len)]
visit=[[False for i in range(col_len)] for j in range(row_len)]

def dump_chart():
    for c in chart:
        print(c)


for i in range(s_num):
    start_col, start_row, end_col, end_row = map(int, sys.stdin.readline().split())
    # row col
    for i in range(start_row, end_row):
        for j in range(start_col, end_col):
            chart[row_len-i-1][j]=-1
    #dump_chart()
    #print()

def bfs(start_row, start_col, cnt):
    global row_len, col_len
    que=deque()
    que.append((start_row, start_col))
    visit[start_row][start_col]=True
    chart[start_row][start_col]=cnt
    d_r=[-1, 1, 0, 0]
    d_c=[0, 0, 1, -1]

    while que:
        now_row, now_col = que.popleft()

        for i in range(4):
            new_row=now_row+d_r[i]
            new_col=now_col+d_c[i]

            if 0<=new_row<row_len and 0<=new_col<col_len and not visit[new_row][new_col] and chart[new_row][new_col] == 0:
                visit[new_row][new_col]=True
                chart[new_row][new_col]=cnt
                que.append((new_row, new_col))
cnt=1
for i in range(row_len):
    for j in range(col_len):
        if chart[i][j]==0:
            bfs(i, j, cnt)
            cnt+=1

ans=defaultdict(int)

for i in range(row_len):
    for j in range(col_len):
        if chart[i][j] > 0:
            ans[chart[i][j]]+=1


#dump_chart()

print(cnt-1)
t = list(sorted(ans.values()))
print(" ".join([str(x) for x in t]))