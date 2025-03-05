# state를 서술해야 한다.
# 
import sys
input=sys.stdin.readline
n=int(input())

dp=[]
INF=99999999999
def cal(li, start, end):
    global dp, prefix_sum
    if end - start == 1:
        return 0
    if dp[start][end] != INF:
        return dp[start][end]
    mini=INF
    for i in range(start+1, end):
        mini = min(mini, cal(li, start, i) + cal(li, i, end))
    dp[start][end]=prefix_sum[end] - prefix_sum[start] + mini
    return dp[start][end]


for _ in range(n):
    length=int(input())
    li=list(map(int, input().split()))
    dp=[[INF for i in range(length+1)] for i in range(length+1)]
    prefix_sum=[0 for i in range(length+1)]

    for i in range(length):
        prefix_sum[i+1]=li[i]
    for i in range(1, length+1):
        prefix_sum[i]+=prefix_sum[i-1]

    print(cal(li, 0, length))