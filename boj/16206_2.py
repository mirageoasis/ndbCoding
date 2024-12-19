n, knife = map(int, input().split())
li = list(map(int, input().split()))

li.sort(key=lambda x: (x % 10, x))
ans=0
for i in li:
    if knife == 0:
        break
    
    if i == 10:
        ans+=1
        continue
    
    while i >= 10:
        if i == 10:
            ans+=1
            break
        if knife == 0:
            break
        i -= 10
        ans+=1
        knife-=1

print(ans)