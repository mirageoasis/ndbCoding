import sys
k, n = map(int, input().split())


start=0
end=2**31
li=[]
for i in range(k):
    li.append(int(sys.stdin.readline()))
ans=0
while start < end:
    mid=(start+end)//2
    res=sum([i//mid for i in li])
    #print(start, end, mid, res, n)
    if res >=n:
        ans=mid
        start=mid+1
    else:
        end=mid

print(ans)