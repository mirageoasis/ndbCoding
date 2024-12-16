n, m=map(int, input().split())
li=list(map(int, input().split()))

ans=sum(li[:m])
now=ans
for i in range(1, n-m+1):
    minus=li[i-1]
    plus=li[i+m-1]
    now-=minus
    now+=plus
    ans=max(now, ans)

print(ans)