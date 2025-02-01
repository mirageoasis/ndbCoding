n, m = map(int, input().split())
li=[]
import sys
for _ in range(n):
    li.append(int(sys.stdin.readline()))
li.sort()

start=0
end=1
ans=2_000_000_001
while True:
    s=li[end]-li[start]
    if s <= m:
        if m == s:
            ans=m
        if end == n-1:
            break
        end+=1
    else:
        start+=1
        ans=min(ans, s)
print(ans)