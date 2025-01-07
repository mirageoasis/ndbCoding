n=int(input())
li=[]

for i in range(n):
    a, b = map(int, input().split())
    li.append(b-a)

li.sort()
ans=10**11
for i in range(len(li)-1):
    ans=min(ans, li[i+1] - li[i]+1)

print(ans)