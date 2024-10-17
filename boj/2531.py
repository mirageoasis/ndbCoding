# 4시 37분
import sys


N, sushi_kind, limit, coupon = map(int, input().split())
chart=[]
count=[0 for i in range(sushi_kind+1)]

for i in range(N):
    chart.append(int(sys.stdin.readline().strip()))

ans=0
#print(chart)
def total_count():
    global ans, N, sushi_kind, limit, coupon, chart

    # 0 부터 시작
    t=set()
    for i in range(limit):
        count[chart[i]]+=1
        t.add(chart[i])
    t.add(coupon)
    count[coupon]+=1
    # 앞 뒤 이동~
    kind=len(t)
    ans=max(ans, kind)
    
    start=0
    end=limit-1
    cnt=0

    while cnt <= N-1:
        #print(count[1:sushi_kind+1])
        #print(kind)
        ans=max(ans, len(t))
        # 최신화 이후 다시 갱
        start = (start+1) % N
        end = (end+1) % N
        
        count[chart[(start-1+N) % N]]-=1
        count[chart[end]]+=1

        if count[chart[(start-1+N) % N]] == 0:
            t.remove(chart[(start-1+N) % N])
        t.add(chart[end])

        cnt+=1


total_count()
print(ans)