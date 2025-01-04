from copy import deepcopy
n, m = map(int, input().split())

chart=[[1 for i in range(n)] for j in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    chart[a-1][b-1]=0
    chart[b-1][a-1]=0

for i in range(n):
    chart[i][i]=0

def all_zero():
    global chart, n
    for i in range(n):
        for j in range(n):
            if chart[i][j]:
                return False
    return True
turn=0
ans=[]
while not all_zero():
    # 1번씩만
    new_chart=deepcopy(chart)
    new_friend=[]
    cnt=0
    for i in range(n):
        # 현재 친구
        now_friends=set([j for j in range(n) if not chart[i][j]]) 
        new_friends=set([k for j in now_friends for k in range(n) if not chart[j][k]])
        total_friend=now_friends | new_friends
        for t in total_friend:
            new_chart[i][t]=0
        #print(total_friend - now_friends)
        cnt+=len(total_friend - now_friends)

    chart=new_chart
    turn+=1
    ans.append(cnt//2)

print(turn)

for a in ans:
    print(a)
