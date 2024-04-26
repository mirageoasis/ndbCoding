import sys

N, H = map(int, input().split(' '))

up = []
down = []
up_chart = [0 for i in range(H+1)]
down_chart = [0 for i in range(H+1)]
chart = [0 for i in range(H+1)]

# 같으면 count x
# up은 위를 향해있다.
# down은 아래를 향해있다.

for i in range(N):
    if i % 2:
        up.append(int(sys.stdin.readline()))
    else:
        down.append(int(sys.stdin.readline()))

for i in up:
    up_chart[i] += 1

for i in down:
    down_chart[H-i+1] += 1

for i in range(H - 2, 0, -1):
    up_chart[i] += up_chart[i + 1]

for i in range(1, H+1):
    down_chart[i] += down_chart[i - 1]

for i in range(H+1):
    chart[i] = up_chart[i] + down_chart[i]

#print(list((idx, i) for idx, i in enumerate(up_chart)))
#print(list((idx, i) for idx, i in enumerate(down_chart)))
#print(list((idx, i) for idx, i in enumerate(chart)))

#for i in range
mini = min(chart[1:])

print(mini, chart[1:].count(mini))