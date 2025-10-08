n, m, k = map(int, input().split())

chart=[]
li=[]

for i in range(n):
    chart.append(list(map(int, input().split())))
    for j in range(m):
        li.append((i, j))
ans=-10000 * 10000
from itertools import combinations
for a in combinations(li, k):
    ban=[]
    d_r=[1, -1, 0, 0]
    d_c=[0, 0, -1, 1]
    for i in a:
        for j in range(4):
            ban.append((i[0] + d_r[j], i[1]+d_c[j]))
    b_set=set(ban)
    flag=True
    for i in a:
        if i in ban:
            flag=False
    if not flag:
        continue
    temp=0
    for i in a:
        temp+=chart[i[0]][i[1]]
    
    ans=max(ans, temp)

print(ans)
