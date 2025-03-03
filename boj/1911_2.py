# 그리디 아닌가? 뒤에 상관없이 지금 메꾸면 좋음
import sys
import math
input=sys.stdin.readline

n, m = map(int, input().split())

chart=[]
for i in range(n):
    chart.append(list(map(int, input().split())))

print(chart)
# 다음 널빤지가 시작할 곳
now_head=0

chart.sort(key=lambda x: (x[0]))
ans=0
for c in chart:
    start=c[0]
    end=c[1]-1
    # 안겹침
    if now_head < start:
        now_head=start
    # 0 1 2 3 4 5 6
    count=math.ceil((end-now_head+1)/m)
    ans+=count
    length=count*m
    #print(now_head, now_head+length, ans)
    #print(start, end)
    now_head=now_head+length
    
    pass

print(ans)