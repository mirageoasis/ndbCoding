s=input()
n=int(input())
d=dict()
import sys
for _ in range(n):
    a, b = sys.stdin.readline().split()
    b=int(b)
    if a in d:
        d[a]=max(d[a], b)
    else:
        d[a]=b

dp=[0 for i in range(len(s)+1)]

for idx in range(0, len(s)+1):
    #now = s[:idx]
    now = ""
    for i in range(idx, len(s)):
        now += s[i]
        #print(now)
        if now in d:
            dp[i+1] = max(dp[i+1], dp[idx]+d[now])
        else:
            dp[i+1] = max(dp[i+1], dp[i]+1)

print(dp[-1])