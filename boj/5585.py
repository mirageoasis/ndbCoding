n=int(input())
n=1000-n

li=[500, 100, 50, 10,5, 1]
idx=0
ans=0
while n:
    quota=n // li[idx]
    if quota:
        n-=quota * li[idx]
        ans+=quota
    else:
        idx+=1

print(ans)