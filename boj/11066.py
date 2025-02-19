# state를 서술해야 한다.
# 
import sys
input=sys.stdin.readline
n=int(input())

dp=[]

def cal(li, start, end):
    global dp, prefix_sum
    # end가 뒤에 미포함
    # [start, end)
    
    if dp[start][end] != 99999999999:
        return dp[start][end]
    if end-start == 1:
        return 0
    if end-start == 2:
        dp[start][end]=li[end-1] + li[start]
        return dp[start][end]
    mini=99999999999
    for i in range(start+1, end):
        mini=min(mini, cal(li, start, i) + cal(li, i, end))
    
    dp[start][end]=mini + prefix_sum[end]-prefix_sum[start]
    return dp[start][end]


for _ in range(n):
    length=int(input())
    li=list(map(int, input().split()))
    dp=[[99999999999 for i in range(length+1)] for i in range(length+1)]
    prefix_sum=[0 for i in range(length+1)]

    for i in range(length):
        prefix_sum[i+1]=li[i]
    for i in range(1, length+1):
        prefix_sum[i]+=prefix_sum[i-1]

    print(cal(li, 0, length))