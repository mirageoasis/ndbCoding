n,m=map(int, input().split())
li=list(map(int, input().split()))

ans=0
visit=[False for i in range(n)]
def cal(idx):
    global ans, visit, n, m
    if idx == n:
        temp=0
        cnt=0
        for i in range(n):
            if visit[i]:
                temp+=li[i]
                cnt+=1
        if cnt == 0:
            return
        if temp == m:
            ans+=1
        return
    
    cal(idx+1)
    visit[idx]=True
    cal(idx+1)
    visit[idx]=False

cal(0)
print(ans)