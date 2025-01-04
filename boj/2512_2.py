n=int(input())
li=list(map(int, input().split()))
budget=int(input())

start=0
end=1_000_000_001
ans=0

while start < end:
    mid=(start+end)//2
    s=sum([min(i, mid) for i in li])

    if s <= budget:
        ans=max(ans, mid)
        start=mid+1
    else:
        end=mid

print(ans if sum(li) > budget else max(li))