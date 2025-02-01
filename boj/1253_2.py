n=int(input())
li=list(map(int, input().split()))
li.sort()
s=set()
ans=0
for i in range(n):
    start=0
    end=n-1
    flag=False
    while start!=end:
        if li[start]+li[end] > li[i]:
            end-=1
        elif li[start]+li[end] < li[i]:
            start+=1
        else:
            if start == i:
                start+=1
            elif end == i:
                end-=1
            else:
                flag=True
                break
    if flag:
        #print(li[i])
        ans+=1
print(ans)