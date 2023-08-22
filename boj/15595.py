import sys
from collections import defaultdict

N=int(input())

visit = set()

times = defaultdict(int)

chart = []

for i in range(N):
    _, id, code, mem, a, b, c = sys.stdin.readline().strip().split()

    if id == 'megalusion':
        continue
    chart.append([_, id, int(code), mem, a, b, c])

chart.sort(key=lambda x : x[1])

for i in chart:
    _, id, code, mem, a, b, c = i

    if code != 4 and (id not in visit):
        times[id]+=1
    elif code == 4:
        visit.add(id)
    else:
        continue

if len(visit):
    wrong = sum([value for key, value in times.items() if key in visit])
    print(len(visit) / (len(visit) + wrong) * 100)
else:
    print(0)