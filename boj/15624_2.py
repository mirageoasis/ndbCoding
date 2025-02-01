n, m = map(int, input().split())
li=list(map(int, input().split()))

visit=[False for i in range(n)]
li.sort()

def cal(idx, now):
    global n, m, li, visit
    if idx == m:
        print(*now)
        return

    for i in range(n):
        if not visit[i]:
            visit[i]=True
            now[idx]=li[i]
            cal(idx+1, now)
            now[idx]=0
            visit[i]=False
    

cal(0, [0 for i in range(m)])