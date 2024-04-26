import sys

N, K, M = map(int, input().split(' '))

li = []

for i in range(N):
    li.append(int(sys.stdin.readline().strip()))

filtered = []

for i in li:
    if i >= 2 * K:
        res = i - 2 * K
    else: 
        res = i - K
    filtered.append(res)

filtered = [f for f in filtered if f > 0]
filtered.sort()
ans = 0

if len(filtered) > 0:

    maxi = filtered[-1]

    start = 1
    end = filtered[-1]

    while start <= end:
        mid = (start + end) // 2
        if mid <= 0 or end <= 0:
            break
        res = sum([i // mid for i in filtered])
        if res >= M:
            ans = max(mid, ans)
            start = mid + 1
        else:
            end = mid - 1

if ans == 0:
    print(-1)
else:
    print(ans)
