import sys

N, M = map(int, input().split())

height = list(map(int, sys.stdin.readline().split()))
plus = [0 for i in range(N)]

command = []

for i in range(M):
    command.append(list(map(int, sys.stdin.readline().split())))


for start, end, val in command:
    start = start - 1
    end = end - 1
    plus[start] += val
    if end + 1 < N:
        plus[end + 1] -= val

s = 0

for idx, val in enumerate(plus):
    s += val
    height[idx] += s

print(*height)