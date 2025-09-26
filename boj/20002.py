# 1
# a, b까지 구하기

n=int(input())

chart=[]
dp=[[0 for i in range(n+1)] for j in range(n+1)]
for _ in range(n):
    chart.append(list(map(int, input().split())))
# col 방향

for i in range(1, n+1):
    dp[i][1]=chart[i-1][0]
for i in range(1, n+1):
    dp[1][i]=chart[0][i-1]

# for k in dp:
#     print(k)

for i in range(1, n+1):
    for j in range(1, n+1):
        dp[i][j]=dp[i][j-1]+chart[i-1][j-1]
# print()
# for k in dp:
#     print(k)
# print()
for i in range(1, n+1):
    for j in range(1, n+1):
        dp[i][j]+=dp[i-1][j]

# for k in dp:
#     print(k)

# 0~(a, b) 까지 합
ans=-100001
for row in range(n):
    for col in range(n):
        for k in range(1, n+1):
            end_row=row+k
            end_col=col+k
            if end_row > n or end_col > n:
                break
            # row, col에서 시작
            # end_row, end_col에서 끝
            #print(row, col, k, end_row, end_col,dp[end_row][end_col],dp[end_row][col],dp[row][end_col],dp[row][col])
            ans=max(ans,dp[end_row][end_col]-dp[end_row][col]-dp[row][end_col]+dp[row][col])

print(ans)