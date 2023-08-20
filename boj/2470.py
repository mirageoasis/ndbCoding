N=int(input())

li = list(map(int, input().split()))

li.sort(key=lambda x : abs(x))

t = 1000000000000000
(ans1, ans2) = li[0], li[1]

for i in range(1, N):
    prev = li[i-1]
    now = li[i]
    if t > abs(prev + now):
        ans1 = prev
        ans2 = now
        t = abs(prev + now)

ans1, ans2 = min(ans1, ans2), max(ans1, ans2)

print(ans1, ans2)