N = int(input())

li = list(map(int, input().split()))

lo = 0
hi = N - 1

while lo <= hi:
    mid = (lo + hi) // 2
    #print(mid, li[mid])
    if li[mid] == mid:
        print(mid)
        break
    elif li[mid] > mid:
        hi = mid - 1
    else:
        lo = mid + 1
else:
    print(-1)