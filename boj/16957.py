import sys
from collections import deque

R, C = map(int, input().split())

chart = []
ball = [[1 for i in range(C)] for j in range(R)]
dp = [[(-1, -1) for i in range(C)] for j in range(R)]

for i in range(R):
    chart.append(list(map(int, sys.stdin.readline().split())))

def dfs(start_row, start_col, now_row, now_col, R, C, chart, ball, dp):
    dest_r, dest_c = dp[now_row][now_col]
    if dest_r != -1 and dest_c != -1:
        ball[dest_r][dest_c] += 1
        ball[start_row][start_col] -= 1
        dp[start_row][start_col] = (dest_r, dest_c)
        return
    
    d_r = [0, 0, -1, 1, 1, 1, -1, -1]
    d_c = [-1, 1, 0, 0, -1, 1, 1, -1]
    
    ans_row = now_row
    ans_col = now_col

    for i in range(8):
        new_row = now_row + d_r[i]
        new_col = now_col + d_c[i]
        if  0 <= new_row < R and 0 <= new_col < C:
            if chart[ans_row][ans_col] > chart[new_row][new_col]:
                ans_row = new_row
                ans_col = new_col
                
    if ans_row == now_row and ans_col == now_col:
        ball[now_row][now_col] += 1
        ball[start_row][start_col] -= 1
        dp[now_row][now_col] = (now_row, now_col)
        return
    
    dfs(start_row, start_col, ans_row, ans_col, R, C, chart, ball, dp)

for i in range(R):
    for j in range(C):
        dfs(i, j, i, j, R, C, chart, ball, dp)


for i in ball:
    print(*i)