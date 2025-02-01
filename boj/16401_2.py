m, n = map(int, input().split())
li=list(map(int, input().split()))

INF=1_000_000_001

start=0
end=INF
ans=0
while start < end:
    mid=(start+end)//2
    if mid == 0:
        break

    cnt=sum([i//mid for i in li])
    if cnt >= m:
        ans=max(ans, mid)
        start=mid+1
    else:
        end=mid
    pass

print(ans)