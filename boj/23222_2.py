n, k = map(int, input().split())
li=list(map(int, input().split()))

flag=True
ans=0
cnt=0
while flag:
    idx=0
    flag=False
    #print(li)
    while idx + k < len(li):
        if li[idx + k] - li[idx]:
            flag=True
            ans+=li[idx + k] - li[idx]
            cnt+=1
            if idx + k + 1 < n:
                li=li[:idx] + [li[idx]] + li[idx:idx+k] + li[idx+k+1:]
            else:
                li=li[:idx] + [li[idx]] + li[idx:idx+k]
            break
        idx+=1
    
print(ans, cnt)