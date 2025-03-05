import sys
input=sys.stdin.readline

maxi=int(input())
n=int(input())
INF=2**31-1
dist=list(map(int, input().split()))
time=list(map(int, input().split()))
time.insert(0, 0)
time.append(0)
#100 30 100  40  50  60
#0 5  10   4  11   7  0

dp=[INF for i in range(n+2)]

def cal(index):
    global dp, INF, maxi, dist, time
    if index == 0:
        return 0
    if dp[index] != INF:
        return dp[index]
    d=0
    for i in range(index-1, -1,-1):
        d+=dist[i]
        if d > maxi:
            break
        dp[index]=min(dp[index], cal(i))
    dp[index]+=time[index]
    return dp[index]

print(cal(len(time)-1))
dp[0]=0
ans=[]
idx=len(time)-1
#print(time)
#print(dp)
while idx:
    for j in range(idx-1, -1, -1):
        if dp[idx] == time[idx] + dp[j]:
            ans.append(j)
            idx=j
            break
ans.pop()
ans.reverse()
print(len(ans))
print(*ans)