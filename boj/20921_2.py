n, m = map(int, input().split())

origin=[i for i in range(1, n+1)]

if m == 0:
    print(*origin)
else:
    # m 
    pick_list=[]
    now_can=len(origin) - 1

    while now_can:
        if m >= now_can:
            pick_list.append(now_can+1)
            m-=now_can
        now_can-=1
    t= pick_list + [i for i in range(1, n+1) if i not in set(pick_list)]
    print(*t)
