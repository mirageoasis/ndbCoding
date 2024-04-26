# 고기 개수, 필요 고기 양
import sys


N, M = map(int, input().split())

# 무게, 가격 순
chart = []

for i in range(N):
    weight, cost = map(int, sys.stdin.readline().split())
    chart.append((weight, cost))

chart.sort(key=lambda x : (x[1], -x[0]))

s = 0
prev_cost = 0
now_cost=0
INF=2147483690
ans=INF
for weight, cost in chart:
    s+=weight
    if cost > prev_cost:
        if s >= M:
            ans=min(cost, ans)
        prev_cost=cost
        now_cost=cost
    else:
        # cost 같은 시기가 유지가 될 때
        now_cost+=cost
        if s >= M:
            ans=min(now_cost, ans)
    #print(s, M, now_cost, cost)
if ans == INF:
    print(-1)
else:
    print(ans)