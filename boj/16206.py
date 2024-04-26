N, M = map(int, input().split())

li = sorted(list(map(int, input().split())), key=lambda x : (x % 10, x))

ans = 0

for i in li:
    left = i
    while left > 10 and M > 0:
        ans+=1
        M-=1
        left -= 10
    
    if left == 10:
        ans+=1


print(ans)