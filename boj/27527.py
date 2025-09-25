from math import ceil

n, m = map(int, input().split())
li=list(map(int, input().split()))


cnt=[0 for i in range(10**6+1)]
flag=False
for i in range(m):
    cnt[li[i]]+=1
    if cnt[li[i]] >= ceil(9*m/10):
        flag=True
        break

for i in range(m, n):
    added=li[i]
    dele=li[i-m]
    cnt[dele]-=1
    cnt[added]+=1

    if cnt[added] >= ceil(9*m/10):
        flag=True
        break

print("YES" if flag else "NO")