num=int(input())

s=0
ans=0
for i in range(1, num+1):
    if s + i > num:
        break
    else:
        s+=i
        ans+=1

print(ans)