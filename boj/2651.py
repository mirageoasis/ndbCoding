# 냅섹?
"""
dp[n] -> n일 때 최소

dp[n]안에서 -> dp[1]까지 줄이면서 최소값을 찾아주기
"""
import sys
input=sys.stdin.readline

max_dist=int(input())
n=int(input())
n+=2

# i 지점 거리
li=list(map(int, input().split()))
li.append(0)

for i in range(len(li)-2,-1,-1):
    li[i]+=li[i+1]

# i 지점 수리 시간
time=list(map(int, input().split()))
time.insert(0,0)
time.append(0)

#print(li)
#print(time)

# i번 point에 오기까지 걸린 최소 값
INF=2**31-1
dp=[INF for i in range(n)]

def cal(index):
    global n, max_dist, li, time
    if index == 0:
        dp[0]= 0
        return 0
    if dp[index] != INF:
        return dp[index]
    for i in range(index-1, -1, -1):
        if li[i] - li[index] > max_dist:
            break
        dp[index]=min(dp[index], time[index]+cal(i))
    return dp[index]

print(cal(len(li)-1))
ans=[]
target=dp[-1]
for i in range(len(li)-2, -1, -1):
    if dp[i] == target:
        ans.append(i)
        target=dp[i]-time[i]

#print(ans)
ans.pop()
ans.sort()

print(len(ans))
print(*ans)