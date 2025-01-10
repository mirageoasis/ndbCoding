n, m = map(int, input().split())
li=list(map(int, input().split()))

li.sort()
start=0
end=len(li)-1
ans=0
while start<end:
    if li[start]+li[end] >= m:
        start+=1
        end-=1
        ans+=1
    else:
        start+=1

print(ans)