n, m, length = map(int, input().split())
li=list(sorted(map(int, input().split())))
li.insert(0, 0)
li.append(length)
#print(li)
dist=[]

for i in range(n+1):
    dist.append(li[i+1]-li[i])

start=1
end=max(dist)
ans=max(dist)
#print(dist)
import math
while start < end:
    mid=(start+end)//2
    cal=sum([(d-1)//mid for d in dist])
    #print(mid, cal)
    if cal > m:
        start=mid+1
    else:
        ans=min(ans, mid)
        end=mid

print(ans)