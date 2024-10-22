# 4시 37분
import sys


N, sushi_kind, limit, coupon = map(int, input().split())
chart=[]
count=[0 for i in range(sushi_kind+1)]

for i in range(N):
    chart.append(int(sys.stdin.readline().strip()))

#print(chart)
def total_count():
    global ans, N, sushi_kind, limit, coupon, chart

    # 0 부터 시작
    ans=0
    t=set()
    for i in range(limit):
        count[chart[i]]+=1
        t.add(chart[i])
    t.add(coupon)
    count[coupon]+=1
    # 앞 뒤 이동~
    kind=len(t)
    ans=kind
    
    start=1
    end=limit%N
    cnt=1

    while cnt <= N-1:
        #print(count[1:sushi_kind+1])
        #print(chart[start:end+1])
        count[chart[(start-1+N) % N]]-=1
        if count[chart[(start-1+N) % N]] == 0:
            kind-=1
        # 출발 제거해보고 0이면 out
        count[chart[end]]+=1
        if count[chart[end]] == 1:
            kind+=1
        
        
        ans=max(ans, kind)

        start = (start+1) % N
        end = (end+1) % N

        cnt+=1


total_count()
print(ans)