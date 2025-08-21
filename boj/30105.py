from collections import defaultdict

n=int(input())
li=list(map(int, input().split()))

d=defaultdict(set)

for i in range(len(li)):
    for j in range(i+1, len(li)):
        diff = li[j] - li[i]
        d[diff].add(i)
        d[diff].add(j)
ans=[]
for k, v in d.items():
    if len(v) >= len(li):
        ans.append(k)

print(len(ans))
print(*ans)