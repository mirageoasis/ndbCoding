n, k =map(int, input().split())
days=list(map(int, input().split()))

# 10 ** 6
# 1000 1000 
# 10 ^ 6 동안 계산
# 다음에 올 때까지 코인 가격을 계산

start=0
end=6
end=10**18+1

while start < end:
    mid=(start+end)//2

    #days
    # 이전
    cal=mid
    for i in range(1, len(days)):
        prev=days[i-1]
        now=days[i]
        if now - prev >= mid:
            cal+=(mid - 1) * (mid) // 2
        else:
            cal+=(mid - 1) * (mid) // 2 - (mid - (now - prev)) * (mid - (now - prev) + 1) // 2
        cal+=mid
        #print(cal)
    cal+=(mid - 1) * (mid) // 2
    #print()
    #print(cal)
    if cal >= k:
        end=mid
    else:
        start=mid+1

print(start)