# 1000 * 1000

import sys

n=int(input())
li=[]
chart=[0 for i in range(367)]
for i in range(n):
    li.append(list(map(int, sys.stdin.readline().split())))

li.sort(key=lambda x: (x[0], -x[1]))


for st, ed in li:
    for i in range(st, ed+1):
        chart[i]+=1


height=0
ans=0
start=li[0][0]
for i in range(1, 367):
    if chart[i] != 0:
        height = max(height, chart[i])
    else:
        ans+= (i - start) * height
        start=i+1
        height=0


print(ans)