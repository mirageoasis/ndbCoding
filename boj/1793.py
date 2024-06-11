from sys import stdin

LIM=251

dp=[0 for i in range(LIM)]
dp[0]=1
dp[1]=1
dp[2]=3

for i in range(3, LIM):
    dp[i]=dp[i-2]*2+dp[i-1]


while True:
    try:
        N = int(input())
        print(dp[N])
    except:
        break