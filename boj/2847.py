n=int(input())
li=[]
for i in range(n):
    li.append(int(input()))

should_be=li[-1]
ans=0
for i in range(len(li)-1, -1, -1):
    if li[i] < should_be:
        should_be=li[i]
    else:
        ans+=(li[i]-should_be)
    should_be-=1

print(ans)