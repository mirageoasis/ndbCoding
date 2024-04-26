import sys

N, K = map(int, input().split())

li = []

for i in range(N):
    li.append(int(sys.stdin.readline().strip()))

ans = 0
start = 1
last = max(li)

while start <= last:
    mid = (start + last) // 2
    # 나눠줄 수 있는 명수
    s = sum([i // mid for i in li])

    if s >= K:
        start = mid + 1
        ans = max(ans, mid)
    else:
        last = mid - 1

print(ans)