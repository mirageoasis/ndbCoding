import sys

N, K = map(int, input().split(' '))

li = []

for i in range(N):
    li.append(int(sys.stdin.readline().strip()))

start = 1
end = 2 ** 31 - 1


while True:
    mid = (start + end) // 2

    if start > end:
        break

    val = sum([i // mid for i in li])
    
    if val >= K:
        ans = mid
        start = mid + 1
    else:
        end = mid - 1

print(ans)