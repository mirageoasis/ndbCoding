n=int(input())

dp=[[[-1 for i in range(5)] for j in range(10)] for k in range(n+1)]

"""
0 -2 증가
1 -1 증가
2 0 증가
3 1 증가 
4 2 증가
"""
MOD=1_000_000_007
def cal(index, number, streak_cnt):
    if streak_cnt == 2:
        if index == 1:
            dp[index][number][streak_cnt]=1
            return dp[index][number][streak_cnt]
        return 0
    
    if index == 1:
        dp[index][number][streak_cnt]=0
        return dp[index][number][streak_cnt]
    
    if dp[index][number][streak_cnt] != -1:
        return dp[index][number][streak_cnt]
    dp[index][number][streak_cnt]=0
    if streak_cnt == 4:
        if number != 0:
            dp[index][number][streak_cnt]=cal(index-1, number-1, 3)
            return dp[index][number][streak_cnt]
    elif streak_cnt == 3:
        if number != 0:
            dp[index][number][streak_cnt]+=cal(index-1, number-1, 2)
            dp[index][number][streak_cnt]%=MOD
            dp[index][number][streak_cnt]+=cal(index-1, number-1, 1)
            dp[index][number][streak_cnt]%=MOD
            dp[index][number][streak_cnt]+=cal(index-1, number-1, 0)
            dp[index][number][streak_cnt]%=MOD
            return dp[index][number][streak_cnt]
    elif streak_cnt == 1:
        if number != 9:
            dp[index][number][streak_cnt]+=cal(index-1, number+1, 2)
            dp[index][number][streak_cnt]%=MOD
            dp[index][number][streak_cnt]+=cal(index-1, number+1, 4)
            dp[index][number][streak_cnt]%=MOD
            dp[index][number][streak_cnt]+=cal(index-1, number+1, 3)
            dp[index][number][streak_cnt]%=MOD
            return dp[index][number][streak_cnt]
    elif streak_cnt == 0:
        if number != 9:
            dp[index][number][streak_cnt]=cal(index-1, number+1, 1)
            return dp[index][number][streak_cnt]
    return 0



ans=0
for i in range(10):
    for j in range(5):
        ans+=cal(n, i, j)
        ans%=MOD

print(ans)
