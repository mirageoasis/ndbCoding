import sys

n, m = map(int, input().split())

li=[]

for i in range(n):
    li.append(int(sys.stdin.readline()))

start=0
end=2**31
ans=0

while start<end:
    mid=(start+end)//2
    if mid == 0:
        break
    temp=sum([int(i)//mid for i in li])

    if temp >= m:
        ans=max(ans, mid)
        start=mid+1
    else:
        end=mid

print(ans)