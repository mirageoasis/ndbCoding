# dp 이거나
# 완탐? 범위가 작아서?

n, m = map(int, input().split())

first=[]
second=[]

for i in range(n):
    first.append(list(map(int, input().split())))

for i in range(n):
    second.append(list(map(int, input().split())))


INF=256 * 256 * 111
dp=[[INF for i in range(m)] for j in range(n)]

# 행마다 계산

def cal(row, col, num):
    global dp, n, m, INF
    if row == 0:
        dp[row][col]=(first[row][col] - second[row][col]) ** 2
        return dp[row][col]
    if dp[row][col] != INF:
        return dp[row][col]
    ret=INF
    if col + 1 < m:
        ret=min(ret, cal(row-1, col+1, num))
    if col - 1 > -1:
        ret = min(ret, cal(row-1, col-1, num))
    ret = min(ret, cal(row-1, col, num))
    dp[row][col] = (first[row][col] - second[row][col]) ** 2 + ret
    return dp[row][col]


ans=INF
for col in range(m):
    ans=min(ans, cal(n-1, col, 0))


print(ans)