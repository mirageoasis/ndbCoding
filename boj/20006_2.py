# k는 인원 제한
n, k = map(int, input().split())
chart=[[] for i in range(300)]

def find_idx(lvl):
    global k
    for idx, val in enumerate(chart):
        if len(val) == 0:
            return idx
        elif val[0][1]-10 <= lvl <= val[0][1]+10 and len(val) < k:
            return idx


for i in range(n):
    lvl, nick = input().split()
    lvl=int(lvl)
    finder_idx=find_idx(lvl)

    chart[finder_idx].append((nick, lvl))


for c in chart:
    if len(c) == 0:
        break
    #print(len(c))
    if len(c) == k:
        print("Started!")
    else:
        print("Waiting!")
    
    c.sort(key=lambda x: (x[0]))
    for a in c:
        print(a[1], a[0])