n, first, second = map(int, input().split())

visit=[False for i in range(n*2)]

init_num=second-first-1

visit[first-1]=True
visit[second-1]=True
ans=0

def cal(idx):
    global visit, n, init_num, ans
    #print(idx)
    if idx == n+1:
        ans+=1
        return

    if idx != init_num:
        for i in range(2*n-idx-1):
            if not visit[i] and not visit[i+idx+1]:
                visit[i+idx+1]=True
                visit[i]=True
                cal(idx+1)
                visit[i]=False
                visit[i+idx+1]=False
    else:
        cal(idx+1)

cal(1)

print(ans)