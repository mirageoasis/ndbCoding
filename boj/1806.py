# 이진탐색으로 풀 수도 있다.
N, M = map(int, input().split())
chart = list(map(int, input().split()))

start=0
end=0
s=0
ans=N+1

while True:
    #print(ans, end-start)
    #print(chart[start: end], s)
    if s >= M:
        if start == N:
            break
        ans=min(ans, end-start)
        s-=chart[start]
        start+=1
    else:
        if end == N:
            break
        s+=chart[end]
        end+=1


if ans != N+1:
    print(ans)
else:
    print(0)