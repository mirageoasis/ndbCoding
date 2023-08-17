from heapq import heappop, heappush, heapify

N, M = map(int, input().split())

flag = False

present = list(map(int, input().split()))
child_demand = list(map(int, input().split()))

present = [-p for p in present]

heapify(present)

for c in child_demand:
    p = abs(heappop(present))
    if p < c:
        flag = True
        break
    else:
        t = p - c
        heappush(present, -t)

if flag:
    print(0)
else:
    print(1)