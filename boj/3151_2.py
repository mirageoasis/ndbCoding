from bisect import bisect_left, bisect_right
n=int(input())
li=list(map(int, input().split()))
li.sort()
ans=0

for i in range(n):
    for j in range(i):
        target=li[i]+li[j]
        left=bisect_left(li, -target, 0, j)
        right=bisect_right(li, -target, 0, j)
        ans+=(right-left)

print(ans)