import sys
input=sys.stdin.readline

n=int(input())
chart=[[False for i in range(11)]for j in range(n)]
dp=[[-1 for i in range(11)] for j in range(n)]

for i in range(n):
    li=list(map(int, input().split()))
    li=li[1:]
    for j in li:
        chart[i][j]=True
    

def cal(row, col):
    global dp, n, chart
    if dp[row][col] != -1:
        return dp[row][col]
    if row == n - 1:
        dp[row][col] = col
        return dp[row][col]

    for i in range(1, 11):
        if chart[row + 1][i] and i != col:
            ret = cal(row+1, i)
            if ret > 0:
                dp[row][col] = ret * 10 + col
                return dp[row][col]
    dp[row][col]=0
    return dp[row][col]

for i in range(1, 11):
    if chart[0][i]:
        ret = cal(0, i)
        if ret != 0:
            for k in reversed(str(ret)):
                print(k)
            break
else:
    print(-1)

# for c in chart:
#     print(c)
# print()
# for c in dp:
#     print(c)