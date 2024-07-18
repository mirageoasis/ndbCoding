# 22분
N, K = map(int, input().split())
chart=list(map(int, input().split()))

start=min(chart)
end=sum(chart)
ans=-1


while start <= end:
    # 최소값
    mid=(start+end)//2
    #print(start, end, mid)
    # 한번 탐색 N
    now=0
    div=0
    for c in chart:
        now+=c
        if now>= mid:
            now=0
            div+=1
    #print("divide",div, K)
    if div >= K:
        # 답 아님
        start=mid+1
    else:
        end=mid-1

print(start-1)