from collections import deque
import sys

row_len, col_len = map(int, input().split())

chart=[]
for _ in range(row_len):
    chart.append(list(map(int, sys.stdin.readline().split())))

visit=[[False for i in range(col_len)]for j in range(row_len)]

def bfs(start_row, start_col):
    global visit, chart, row_len, col_len
    que=deque()
    que.append((start_row, start_col))

    d_r=[1, row_len-1, 0, 0]
    d_c=[0, 0, col_len-1, 1]

    while que:
        now_row, now_col = que.popleft()
        for i in range(4):
            new_row=(now_row+d_r[i]) % row_len
            new_col=(now_col+d_c[i]) % col_len
            if not visit[new_row][new_col] and chart[new_row][new_col] == 0:
                visit[new_row][new_col]=True
                que.append((new_row, new_col))

cnt=0
for row in range(row_len):
    for col in range(col_len):
        if not visit[row][col] and chart[row][col] == 0:
            bfs(row, col)
            cnt+=1

print(cnt)