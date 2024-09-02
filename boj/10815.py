N=int(input())
li=list(map(int, input().split()))

M=int(input())
li2=list(map(int, input().split()))

ans=[]

li.sort()

for i in li2:
    start=0
    end=len(li)-1
    flag=False
    while start <= end:
        mid=(start+end) // 2
        if li[mid] == i:
            flag=True
            break
        elif li[mid] > i:
            end=mid-1
        else:
            start=mid+1
    if flag:
        ans.append(1)
    else:
        ans.append(0)


print(' '.join([str(i) for i in ans]))