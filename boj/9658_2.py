n=int(input())

# 선공이 진다면
# 1 3 4를 minus하면 선공이 바뀐 상태니까 1 3 4 중에서
# i - x를 통해 선공이 바뀐 상태에서 게임을 진행한다고 이해하면 된다.
dp = [False for i in range(1001)]

dp[1]=False
dp[2]=True
dp[3]=False
dp[4]=True

for i in range(5, 1001):
    if not dp[i-1]:
        dp[i]=True
    if not dp[i-3]:
        dp[i]=True
    if not dp[i-4]:
        dp[i]=True

#print(dp[n])
print("SK" if dp[n] else "CY")