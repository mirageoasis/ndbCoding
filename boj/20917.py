import sys
input=sys.stdin.readline

t=int(input())

for _ in range(t):
    n, s = map(int, input().split())
    li=list(sorted(list(map(int, input().split()))))

    start=1
    end=1_000_000_001
    ans=-1
    while start < end:
        mid=(start+end)//2
        last=li[0]
        cnt=1
        for i in range(1, n):
            if li[i] - last >= mid:
                last=li[i]
                cnt+=1
        # 결산
        if cnt >= s:
            start=mid+1
            ans=mid
        else:
            end=mid
    print(ans)


