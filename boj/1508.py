import sys
input=sys.stdin.readline
# 역시 최대 최소 나오면 이분탐색부터 의심
n,m,k=map(int, input().split())
li=list(map(int, input().split()))

start=1
end=li[-1]-li[0]+1
ans=""
while start < end:
    #print(start, end, ans)
    mid=(end+start)//2
    tmp=["0" for i in range(k)]
    tmp[0]="1"
    # mid를 달성할 수 없으면 후퇴, m명 배치
    last=li[0]
    cnt=1
    for i in range(1, len(li)):
        if cnt == m:
            break
        if li[i] - last < mid:
            continue
        last=li[i]
        tmp[i]="1"
        cnt+=1
    
    if cnt >= m:
        start=mid+1
        ans=''.join(tmp)
    else:
        end=mid

print(ans)