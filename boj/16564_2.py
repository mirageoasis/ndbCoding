"""
naive하게

x설정 n번 돌면서 하면
1000000 * 1_000_000_000

x 를 늘리면 temp_k도 증가한다.
"""
import sys
n, k = map(int, input().split())
chart=[]

for i in range(n):
    chart.append(int(sys.stdin.readline()))

start=min(chart)
end=2_000_000_001
ans=0
while start<end:
    mid=(start+end)//2
    s=sum([mid - c for c in chart if mid - c > 0])

    if s > k:
        end=mid
    else:
        start=mid+1
        ans=max(ans, mid)

print(ans)