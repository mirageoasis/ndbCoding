n=int(input())
li=list(map(int, input().split()))
cmp=[0 for i in range(n)]


idx=0
cnt=0
while idx < n:
    if cmp[idx] != li[idx]:
        for i in range(3):
            new=idx+i
            if new < n:
                cmp[new]^=1
        cnt+=1
        continue
    idx+=1

print(cnt)