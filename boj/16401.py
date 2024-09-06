M, N = map(int, input().split())
li = list(map(int, input().split()))

start=1
end=1_000_000_000
ans=0

while start<=end:
    mid=(start+end)//2
    if mid == 0:
        break
    s=sum([i//mid for i in li])

    if s >= M:
        start=mid+1
        ans=max(ans, mid)
    else:
        end=mid-1

print(ans)