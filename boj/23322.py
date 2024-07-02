import bisect
from time import sleep

# N
# 
N, K = map(int, input().split())

# K번째 중에서
# K+1부터 계속 더하기?
# 에
li = list(map(int, input().split()))
li.sort()

idx=K
ans=0
cnt=0
#print(0, 0, li)


while True:
    t=li.copy()

    first_idx=idx-K
    second_idx=idx

    for i in range(N-K):
        first_idx=i
        second_idx=i+K

        if li[first_idx] != li[second_idx]:
            ans+=(t[second_idx] - t[first_idx])
            t[second_idx]=t[first_idx]
            break
    t.sort()

    if li == t:
        break

    li=t.copy()


    cnt+=1


print(ans, cnt)