    #33

    M=int(input())
    lines = []
    while True:
        start, end = map(int, input().split())
        if start == 0 and end == 0:
            break
        if max(start, end) == min(start, end):
            continue
        if max(start, end) <= 0:
            continue
        if min(start, end) > M:
            continue

        lines.append((min(start, end), max(start, end)))

    lines.sort(key=lambda x: (x[0], x[1]))
    from collections import deque

    lines = deque(lines)

    #print(lines)
    ans=0
    now_end=0

    while lines:
        now_line=lines.popleft()
        t=[]
        if now_line[0] <= now_end:
            t.append(now_line[1])
        else:
            print(0)
            exit(0)
        while lines:
            if lines[0][0] <= now_end:
                n=lines.popleft()
                t.append(n[1])
            else:
                break
        
        now_end=max(t)
        ans+=1
        if now_end >=M:
            break
        
    if now_end < M:
        print(0)
    else:
        print(ans)