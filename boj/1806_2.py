n, m = map(int, input().split())
li=list(map(int, input().split()))

start=0
end=0
s=0
ans=n+1
while True:
    if s >= m:
        ans=min(ans, end-start)
        s-=li[start]
        start+=1
    else:
        if end == n:
            break
        s+=li[end]
        end+=1


if ans == n+1:
    print(0)
else:
    print(ans)