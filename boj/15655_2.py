n, m = map(int, input().split())
li=list(sorted(map(int, input().split())))
visit=[False for i in range(n)]

def cal(start, pick):
    global n, m, visit, li
    if pick == m:
        for i in range(n):
            if visit[i]:
                print(li[i],end=' ')
        print()
        return

    for i in range(start+1, n):
        visit[i]=True
        cal(i, pick+1)
        visit[i]=False

cal(-1, 0)