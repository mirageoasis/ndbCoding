import sys
sys.setrecursionlimit(3000)
input=sys.stdin.readline


n=int(input())
li=[]
dp=[[-1 for i in range(n+1)] for j in range(n+1)]

for _ in range(n):
    li.append(int(input()))

def cal(start, end, index):
    global li
    if dp[start][end] != -1:
        return dp[start][end]
    if start >= end:
        dp[start][end] = 0
        return dp[start][end]
    dp[start][end] = max(cal(start+1, end, index+1) + li[start] * index, cal(start, end-1, index+1) + li[end-1] * index)
    return dp[start][end]

# [start, end) 일 때 최대값


print(cal(0, n, 1))