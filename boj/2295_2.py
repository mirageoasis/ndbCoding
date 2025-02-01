import sys

n=int(input())

li=[]
for i in range(n):
    li.append(int(sys.stdin.readline()))

ans_set=set()
for i in range(n):
    for j in range(n):
        ans_set.add(li[i]+li[j])
ans=0
for i in range(n):
    for j in range(n):
        if li[i] - li[j] in ans_set:
            ans=max(ans, li[i])

print(ans)