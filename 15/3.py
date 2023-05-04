# 5 3
# 1
# 2
# 8
# 4
# 9

li = []
li2 = []

N, C = map(int, input().split())

for i in range(N):
    li.append(int(input()))

li.sort()

lo = 0
hi = li[-1] - li[0]
ans = 0

while lo <= hi:
    #print("cnt")
    prev = li[0]
    mid = (lo + hi) // 2
    cnt = 1
    
    for i in li:
        if i - prev < mid:
            continue
        else:
            prev = i
            cnt+=1
    
    if cnt < C:
        hi = mid - 1
    else:
        ans = max(ans, mid)
        #print(ans)
        lo = mid + 1

print(ans)