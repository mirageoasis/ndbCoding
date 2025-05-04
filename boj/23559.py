import sys
input=sys.stdin.readline
n, x = map(int, input().split())
chart=[]
for i in range(n):
    chart.append(list(map(int, input().split())))

chart.sort(key=lambda x: (x[1]-x[0]))

x-=n*1000
ans=sum([i[1] for i in chart])
cnt=0
while True:
    if x - 4000 < 0:
        break
    if cnt == n:
        break
    if chart[cnt][1] >= chart[cnt][0]:
        break
    ans+=chart[cnt][0]-chart[cnt][1]
    cnt+=1
    x-=4000

print(ans)