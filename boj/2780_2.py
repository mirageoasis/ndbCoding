t=int(input())

ans=[
    [
    [1,1,1],
    [1,1,1],
    [1,1,1],
    [1]
    ] for i in range(1000+1)
]
MOD=1234567
for i in range(2, 1000+1):
    #1
    ans[i][0][0]=(ans[i-1][0][1] + ans[i-1][1][0]) % MOD
    #2
    ans[i][0][1]=(ans[i-1][0][0] + ans[i-1][1][1] + ans[i-1][0][2]) % MOD
    #3
    ans[i][0][2]=(ans[i-1][0][1] + ans[i-1][1][2]) % MOD

    #4
    ans[i][1][0]=(ans[i-1][0][0] + ans[i-1][1][1] + ans[i-1][2][0]) % MOD
    #5
    ans[i][1][1]=(ans[i-1][0][1] + ans[i-1][2][1] + ans[i-1][1][0]+ ans[i-1][1][2]) % MOD
    #6
    ans[i][1][2]=(ans[i-1][0][2] + ans[i-1][1][1] + ans[i-1][2][2]) % MOD

    #7
    ans[i][2][0]=(ans[i-1][1][0] + ans[i-1][2][1] + ans[i-1][3][0]) % MOD
    #8
    ans[i][2][1]=(ans[i-1][1][1] + ans[i-1][2][0] + ans[i-1][2][2]) % MOD
    #9
    ans[i][2][2]=(ans[i-1][1][2] + ans[i-1][2][1]) % MOD

    #0
    ans[i][3][0]=(ans[i-1][2][0]) % MOD


for _ in range(t):
    num=int(input())
    zero=ans[num][0][0] + ans[num][0][1] + ans[num][0][2]
    one=ans[num][1][0] + ans[num][1][1] + ans[num][1][2]
    two=ans[num][2][0] + ans[num][2][1] + ans[num][2][2]
    three=ans[num][3][0]
    print((one+two+three+zero)%MOD)
