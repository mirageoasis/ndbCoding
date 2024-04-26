N=int(input())
li = list(map(int, input().split()))
lim = int(input())



start=0
end=max(li)
ans=-1

while start<=end:
    mid = (start + end) // 2
    mid_sum = sum([mid if i > mid else i for i in li])
    
    #print([mid if i > mid else i for i in li])
    if mid_sum <= lim:
        ans=max(ans, mid)
        start=mid+1
    else:
        end=mid-1

print(ans)