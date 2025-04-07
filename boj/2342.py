li=list(map(int, input().split()))

# 상태를 어캐 나타낼까?
# dp[index][l][r]
INF=99999999999
dp=[[[INF for i in range(5)] for j in range(5)] for k in range(len(li)+1)]
# chart[x][y] -> x로 부터 y까지
chart=[
    [1, 2, 2, 2, 2],
    [2, 1, 3, 4, 3],
    [2, 3, 1, 3, 4],
    [2, 4, 3, 1, 3],
    [2, 3, 4, 3, 1]
]

def cal(index, l, r):
    global dp, li, INF, chart
    # 맨 처음 위치는 0,0 으로 고정
    if index == 0:
        if l == 0 and r == 0:
            dp[0][0][0]=0
            return 0
        return INF
    if dp[index][l][r] != INF:
        return dp[index][l][r]
    
    # index-1의 위치를 고려해서 이동
    left = cal(index-1, li[index-1], r) + chart[li[index-1]][l]

    right= cal(index-1, l, li[index-1]) + chart[li[index-1]][r]

    dp[index][l][r]=min(right, left)
    return dp[index][l][r]

dp[0][0][0]=0

ans=INF
for k in range(len(li)-1):
    for i in range(5):
        for j in range(5):
            # 왼
            dp[k+1][li[k]][j] = min(dp[k+1][li[k]][j], dp[k][i][j] + chart[i][li[k]])
            # 오
            dp[k+1][i][li[k]] = min(dp[k+1][i][li[k]], dp[k][i][j] + chart[j][li[k]])


for left in range(5):
    for right in range(5):
        ans = min(ans, dp[len(li)-1][left][right])
print(ans)