import sys

n=int(input())

chart=[]
dp=[]

for _ in range(n):
    chart.append(list(map(int, sys.stdin.readline().split())))
    dp.append([-1 for i in range(n)])


def cal(start_row, start_col):
    global n, chart, dp

    if dp[start_row][start_col] != -1:
        return dp[start_row][start_col]
    
    dp[start_row][start_col]=1
    d_r=[1, -1, 0, 0]
    d_c=[0, 0, -1, 1]
    ret=0
    for i in range(4):
        new_row=start_row+d_r[i]
        new_col=start_col+d_c[i]
        if 0<=new_row<n and 0<=new_col<n and chart[new_row][new_col] > chart[start_row][start_col]:
            ret=max(ret, cal(new_row, new_col))
    
    dp[start_row][start_col]+=ret
    return dp[start_row][start_col]

for i in range(n):
    for j in range(n):
        cal(i, j)

ans=-1

for i in range(n):
    ans=max(ans, *dp[i])

print(ans)