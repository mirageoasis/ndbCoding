n=int(input())
li=list(map(int, input().split()))
li.sort()

start=0
end=n-1
ans=li[start]+li[end]

while start < end:
    s= li[start] + li[end]
    if abs(ans) > abs(s):
        ans=s
    if s < 0:
        start+=1
    elif s > 0:
        end-=1
    else:
        ans=0
        break


print(ans)