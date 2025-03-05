import sys

input=sys.stdin.readline

n, m, k = map(int, input().split())
li=list(map(int, input().split()))

start=1
end=n+1
ans=""
while start<end:
    mid=(start+end)//2
    s=li[0]
    cnt=1
    temp_ans="1"
    for i in range(1, len(li)):
        if li[i] - s >= mid:
            temp_ans+="1"
            cnt+=1
            s=li[i]
            if cnt == m:
                break
        else:
            temp_ans+="0"
    if cnt == m:
        start=mid+1
        temp_ans=temp_ans+"0"*(k - len(temp_ans))
        ans=temp_ans
    else:
        end=mid


print(ans)