finish=int(input())
import sys
lines=[]
while True:
    s, e = map(int, sys.stdin.readline().split())
    if s == 0 and e == 0:
        break
    lines.append((min(s, e), max(s,e)))

lines.sort(key=lambda x: (x[0], x[1]))

idx=0
now_end=0
answer=0
while idx < len(lines):
    origin_idx=idx
    max_end=now_end
    while idx < len(lines):
        idx_start, idx_end = lines[idx]
        if idx_start > now_end:
            break
        max_end=max(idx_end, max_end)
        idx+=1
    answer+=1
    now_end=max_end
    #print(now_end)
    if idx == origin_idx:
        break
    if now_end >= finish:
        break
#print(now_end, finish, answer)
if now_end >= finish:
    print(answer)
else:
    print(0)