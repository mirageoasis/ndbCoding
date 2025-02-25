# dp 를 사용한다.

# dp[x][y][z] -> x자리 숫자에서 y 수이며 z번 증가할 때 수. z의 범위는 -2~2이고 0은 -2를 2는 증가가 하지 않음을 4는 2자리 연속으로 증가했음을 의미

n=int(input())
MOD=1_000_000_007
dp=[
    [[-1 for k in range(5)] for j in range(10)] for i in range(n+1)
]

def cal(index, number, dir):
    global MOD
    if index < 1:
        return 0
    if number < 0 or number > 9:
        return 0

    if index==1:
        if dir == 2:
            dp[index][number][dir]=1
        else:
            dp[index][number][dir]=0
        return dp[index][number][dir]
    if dp[index][number][dir] != -1:
        return dp[index][number][dir]

    # 모든 수 탐색
    temp=0
    if dir == 4:
        # 자신보다 작으면서 dir이 3인 경우를 찾기
        temp+=cal(index-1, number-1, 3)
        temp%=MOD
    elif dir == 3:
        # 자신보다 작으면서 dir이 0, 1, 2인 경우를 찾는다.
        temp+=cal(index-1, number-1, 0)
        temp%=MOD            
        temp+=cal(index-1, number-1, 1)
        temp%=MOD
        temp+=cal(index-1, number-1, 2)
        temp%=MOD
    elif dir == 2:        
        # 여기를 합산해준게 틀렸음...
        pass
    elif dir == 1:
        temp+=cal(index-1, number+1, 4)
        temp%=MOD
        temp+=cal(index-1, number+1, 3)
        temp%=MOD
        temp+=cal(index-1, number+1, 2)
        temp%=MOD
    elif dir == 0:
        temp+=cal(index-1, number+1, 1)
        temp%=MOD
    
    dp[index][number][dir]=temp
    return dp[index][number][dir]


ans=0
for i in range(5):
    for j in range(10):
        ans+=cal(n, j, i)
        ans%=MOD

print(ans)