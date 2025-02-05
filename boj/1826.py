import sys
input=sys.stdin.readline
gas_chart=[]
n=int(input())
d=dict()
for i in range(n):
    f,s = map(int, input().split())
    d[f]=s
town, left = map(int, input().split())
# 현재 자신이 갈 수 있는 거리 중에서 제일 연로를 많이 주는 주유소를 고른다.
# 그리고 거리가 town초과하면 stop
# 그리디라고 태그 없었으면 몰랐을 듯
# 음.. 여기에서 여러개 안 집어 먹으면 뒤로 못가는 케이스로 고려해야할 거 같은데?
# 이래서 pq를 해서 앞의 주유소에서 충전했어야 했는데... 하는 경우를 처리하기
from heapq import heappush, heappop
heap=[]
info=[0, left]
ans=0

while info[0] < town:
    if info[0] in d:
        heappush(heap, -d[info[0]])
    
    # 먄약에 0이 되면
    if info[1] == 0:
        if heap:
            oil=-heappop(heap)
            info[1]+=oil
            ans+=1
        else:
            break
    info[0]+=1
    info[1]-=1

if info[0] >= town:
    print(ans)
else:
    print(-1)