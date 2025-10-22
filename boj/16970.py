n, m, kv = map(int, input().split())

# 0 1
# 1 0 제외
li=[]
for i in range(n+1):
    for j in range(m+1):
        li.append((i, j))
from itertools import combinations
from math import gcd
ans=0
for k, v in combinations(li, r=2):
    first=abs(k[0]-v[0])
    second=abs(k[1]-v[1])
    if k[0] == v[0] == 0 or k[1] == v[1] == 0:
        #print(max(first, second)+1)
        if max(first, second) + 1 == kv:
            ans+=1
        continue
    #print(gcd(second, first)+1)
    if gcd(second, first)+1 == kv:
        ans+=1
print(ans)


