import sys
n, target_weight=map(int, input().split())
meat_chart=[]

for i in range(n):
    weight, price = map(int, sys.stdin.readline().split())
    meat_chart.append((weight, price))

meat_chart.sort(key=lambda x: (x[1], -x[0]))
INF=2_147_483_649
ans=INF
if meat_chart[0][0] >= target_weight:
    print(meat_chart[0][1])
else:
    former_total=0
    former_price_weight=0
    former_price_sum=0
    flag=False
    for idx in range(len(meat_chart)):
        now_weight, now_price = meat_chart[idx]
        if idx == 0:
            former_price_weight+=now_weight
            former_price_sum+=now_price
            continue
        
        former_weight, former_price = meat_chart[idx-1]
        if now_price == former_price:
            former_price_weight+=now_weight
            former_price_sum+=now_price
            if former_total + former_price_weight >= target_weight:
                ans=min(ans, former_price_sum)
                flag=True
                #print(former_price_sum)
        else:
            former_total+=former_price_weight
            former_price_weight=now_weight
            former_price_sum=now_price
            #print(former_total, now_weight, target_weight)
            if former_total + now_weight >= target_weight:
                ans=min(ans, now_price)
                flag=True
                #print(now_price)
    if flag:
        print(ans)
    else:    
        print(-1)