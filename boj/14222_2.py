n, k = map(int, input().split())
li=list(map(int, input().split()))

cnt=[0 for i in range(50+1)]

for i in li:
    cnt[i]+=1

for i in range(1, n+1):
    if cnt[i] > 0:
        cnt[i]-=1
    else:
        now=k
        while i - now > 0:
            if cnt[i-now] > 0:
                cnt[i-now]-=1
                break
            now+=k
        else:
            print(0)
            break
else:
    print(1)