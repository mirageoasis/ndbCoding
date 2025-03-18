# dp 근데 이제 어떻게 하지?
# iterative하게 해야하나?
import sys
input=sys.stdin.readline

n=int(input())
chart=[]

for i in range(n):
    chart.append(list(map(int, input().split())))

# dp
# dp[x][y][z]
# x번 차례일 때 y좌표 z좌표 -> x는 1더하면서 modulo연산
ans=0
dp=[]
dp=[[[-1 for i in range(n)] for j in range(n)] for k in range(3)]
# 가지치기를 잘해야하는데.
# 1_000_000_000
dp[0][0][0]=0
ans=0
if n == 1:
    if chart[0][0] == 0:
        ans=1
else:
    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                if chart[i][j] == 0:
                    dp[1][i+1][j]=1
                    dp[1][i][j+1]=1
                else:
                    dp[0][i+1][j]=0
                    dp[0][i][j+1]=0
                continue
            
            for k in range(3):
                if dp[k][i][j] != -1:
                    flag=(k == chart[i][j])
                    nxt=(k+1)%3
                    if flag:
                        dp[k][i][j]+=1
                    now=dp[k][i][j]
                    if i == n - 1 and j == n - 1:
                        continue
                    elif i == n - 1:
                        if flag:
                            dp[nxt][i][j+1]=max(dp[nxt][i][j+1], now)
                        else:
                            dp[k][i][j+1]=max(dp[k][i][j+1], now)
                    elif j == n - 1:
                        if flag:
                            dp[nxt][i+1][j]=max(dp[nxt][i+1][j], now)
                        else:
                            dp[k][i+1][j]=max(dp[k][i+1][j], now)
                    else:
                        if flag:
                            dp[nxt][i+1][j]=max(dp[nxt][i+1][j], now)
                            dp[nxt][i][j+1]=max(dp[nxt][i][j+1], now)
                        else:
                            dp[k][i+1][j]=max(dp[k][i+1][j], now)
                            dp[k][i][j+1]=max(dp[k][i][j+1], now)

    ans=max(dp[0][n-1][n-1],dp[1][n-1][n-1],dp[2][n-1][n-1], 0)

# for i in range(3):
#     for d in dp[i]:
#         print(d)
#     print()

print(ans)