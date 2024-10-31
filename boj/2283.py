# 32분 시작
import sys

n, k = map(int, input().split())

chart=[0 for i in range(1000002)]

for i in range(n):
    a,b=map(int, sys.stdin.readline().split())
    chart[a]+=1
    chart[b]-=1
#print(chart[:20])
for i in range(1, 1000002):
    chart[i]+=chart[i-1]
#print(chart[:20])

start=0
end=0

#su=sum([(b-a) for a, b in chart])
s=0
a, b=0,0
while True:
    if s > k:
        s-=chart[start]
        start+=1
        if start > end:
            break
    else:        
        if s == k:
            #print(start, end)
            a=start
            b=end
            break
        s+=chart[end]
        end+=1
        if end > 1000001:
            break

print(a, b)