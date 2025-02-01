import sys
n=int(input())
chart=[]
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    chart.append([a, b])

chart.sort(key=lambda x: (x[0], x[1]))

ans=0
idx=0
while idx < len(chart):
    # 지금 출발해서 찾을 수 있는 
    start, end = chart[idx]
    #print(start, end)
    idx+=1
    while idx < len(chart):
        new_start, new_end = chart[idx]
        # 마지막 end 갱신
        if new_start <= end:
            end=max(end, new_end)
        else:
            break
        idx+=1
    
    ans+=(end-start)
    #print(ans)


print(ans)