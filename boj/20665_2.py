"""

1시간 -> 60분
720 * 5만
짧은 이용 시간이 먼저
"""
import sys
chart=[]
seat_number,people_number,prefer_seat=map(int, input().split())
prefer_seat-=1

def to_number(string):
    return (int(string[:2]) - 9) * 60 + int(string[2:])

for _ in range(people_number):
    st, ed = sys.stdin.readline().split()
    #print(to_number(st), to_number(ed))
    st=to_number(st)
    ed=to_number(ed)
    t=ed-st
    chart.append((st,ed))
chart.sort(key=lambda x: (x[0], x[1]))

seat=[-1 for i in range(seat_number)]
#print(chart)
INF=9999999

def up_dist(idx):
    global seat
    for i in range(idx-1,-1,-1):
        if seat[i] != -1:
            return idx - i
    return INF

def down_dist(idx):
    global seat, seat_number
    for i in range(idx+1, seat_number):
        if seat[i] != -1:
            return i - idx
    return INF

def dist(idx):
    global seat, seat_number, INF
    up=up_dist(idx)
    down=down_dist(idx)

    if up != INF and down != INF:
        return min(up, down)
    elif up == INF and down != INF:
        return down
    elif up != INF and down == INF:
        return up
    else:
        return INF

def find_seat():
    global seat, seat_number, INF
    max_dist=0
    ret_idx=-1
    for i in range(seat_number-1, -1, -1):
        if seat[i] != -1:
            continue
        
        now_dist=dist(i)
        # INF면 즉시 0으로 배정하고 break
        if now_dist == INF:
            return 0
        if max_dist <= now_dist:
            max_dist=now_dist
            ret_idx=i
    
    return ret_idx

ans=0
now=to_number("0900")
#print(now, to_number("2100"))
while now < to_number("2100"):
    # 나갈 사람 찾기
    warn=False
    for idx, val in enumerate(chart):
        st, ed = val
        if ed == now:
            #print(idx, now)
            if st == ed:
                warn=True
                continue
            target_idx = seat.index(idx)
            seat[target_idx]=-1

    # 앉을 사람 찾기
    for idx, val in enumerate(chart):
        st, ed = val
        if st == now:
            target_idx = find_seat()
            seat[target_idx]=idx
    if seat[prefer_seat] == -1:
        ans+=1
    if warn:
        for idx, val in enumerate(chart):
            st, ed = val
            if ed == now and st == ed:
                target_idx = seat.index(idx)
                seat[target_idx]=-1
    
    now+=1

print(ans)