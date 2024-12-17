import sys
n, k ,m = map(int, input().split())

li=[]

for _ in range(n):
    a=int(sys.stdin.readline())

    if a > k:
        if a >= 2 * k:
            a-=2*k
        else:
            a-=k
        if a != 0:
            li.append(a)

if li:
    # 김밥 길이
    ans=-1
    start=1
    end=max(li)+1

    # 1차 계산

    while start < end:
        mid=(start+end)//2

        cal=sum([i//mid for i in li])

        # 결과가 m보다 같거나 크게 나오면 김밥 길이를 올리는 과정이 필요. 즉, start=mid+1
        # 결과가 m보다 작다면 end=mid 
        if cal >= m:
            start=mid+1
            ans=max(ans, mid)
        else:
            end=mid

    print(ans)
else:
    print(-1)
