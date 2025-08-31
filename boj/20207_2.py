import sys
n=int(input())

chart=[0 for i in range(367)]

for i in range(n):
    s, e = map(int, sys.stdin.readline().split())
    for j in range(s,e+1):
        chart[j]+=1
    #chart[s]+=1
    #chart[e]+=1

ans=0
last=0
max_height=0
for i in range(367):
    if not chart[i]:
        ans+=max_height * (i-last-1)
        last=i
        max_height=0
    else:
        max_height=max(chart[i], max_height)

print(ans)
