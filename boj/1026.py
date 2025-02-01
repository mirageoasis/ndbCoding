n=int(input())
first=list(map(int, input().split()))
second=list(map(int, input().split()))

first.sort()
second.sort(reverse=True)
ans=0
for f, s in zip(first, second):
    ans+=f*s

print(ans)