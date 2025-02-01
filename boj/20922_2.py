n, m = map(int, input().split())
li = list(map(int, input().split()))
cnt=[0 for i in range(100001)]
start=0
end=0
ans=0
while True:
    end+=1
    if end == n+1:
        break
    cnt[li[end-1]]+=1
    now=cnt[li[end-1]]
    if now > m:
        while li[start] != li[end-1]:
            cnt[li[start]]-=1
            start+=1
        cnt[li[start]]-=1
        start+=1
    ans=max(ans, end-start)
print(ans)