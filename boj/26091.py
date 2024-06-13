#42 2명 이상 

N, M = map(int, input().split())
chart = list(map(int, input().split()))
chart.sort()
# 일단 sort를 해서 greedy하게 하는 법

start=0
end=len(chart)-1
ans=0

while start < end:
    if chart[start] + chart[end] >= M:
        start+=1
        end-=1
        ans+=1
    else:
        start+=1


print(ans)