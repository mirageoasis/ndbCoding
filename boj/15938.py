import sys
from collections import deque

input=sys.stdin.readline

start_row, start_col = map(int, input().split())
# t 시간보다 작은 경우를 가정하고
# 좌표를 전부 넣을 수는 없고 시간은 200으로 제한이 되어 있다. 그래서 메모리 초과를 믿고 한번 해볼 수도?
limit=int(input())
home_row, home_col = map(int, input().split())

cnt=int(input())
blocks=set()

for i in range(cnt):
    a, b = map(int, input().split())
    blocks.add((a - home_row + 200, b - home_col + 200))

dp=[[[-1 for k in range(401)] for j in range(401)] for i in range(limit+1)]


def cal(time, row, col):
    global dp, blocks, start_row, start_col
    #print(time, row, col, dp[time][row][col])
    if dp[time][row][col] != -1:
        return dp[time][row][col]
    if dp[time][row][col] == -1:
        dp[time][row][col] = 0
    if time == 0:
        return dp[0][row][col]
    if abs(start_row - row) + abs(start_col - col) > time:
        #print(row, col, start_row, start_col, abs(start_row - row), abs(start_col - col), time)
        #print("NO")
        dp[time][row][col] = 0
        return 0
    print(time, row, col, dp[time][row][col])
    d_r=[-1, 1, 0, 0]
    d_c=[0, 0, -1, 1]
    # limit-1로 찾기
    for i in range(4):
        new_row, new_col = row + d_r[i], col + d_c[i]
        if (new_row, new_col) not in blocks:
            dp[time][row][col]+=cal(time-1,new_row, new_col)
            dp[time][row][col]%=(10**9+7)
    #print(time, row, col, dp[time][row][col])
    return dp[time][row][col]

if abs(home_row - start_row) + abs(home_col - start_col) > limit:
    print(0)
else:
    start_row-=home_row
    start_col-=home_col
    start_row+=200
    start_col+=200
    dp[0][start_row][start_col]=1
    ans=0
    for i in range(1, limit+1):
        ans+=cal(i, 200, 200)
        ans%=(10**9+7)
    #print(cal(limit, 200, 200) + cal(limit - 1, 200, 200), + cal(limit -2, 200, 200))
    #print(start_row - home_row + 200, start_col - home_col + 200)
    #print(blocks)
    print(ans)
