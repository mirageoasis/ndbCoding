import sys
n=int(input())
chart=[]
for i in range(n):
    chart.append(int(sys.stdin.readline()))
chart.sort(reverse=True)

ans=0

for i in range(n):
    ans = max(ans, chart[i] * (i+1))

print(ans)