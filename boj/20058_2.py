# 25분

# 일단 돌리는 연산
# 녹이는 연산
from copy import deepcopy

n, command_count=map(int, input().split())
n=2**n
chart=[]

def dump():
    global chart
    for c in chart:
        print(c)


for i in range(n):
    chart.append(list(map(int,input().split())))

commands = list(map(int, input().split()))

def turn(start_row, start_col, length):
    sub2_chart=[[0 for i in range(length)] for j in range(length)]
    sub_chart=[[0 for i in range(length)] for j in range(length)]

    for i in range(start_row, start_row+length):
        for j in range(start_col, start_col+length):
            sub2_chart[i-start_row][j-start_col] = chart[i][j]
            #sub_chart[i-start_row][j-start_col] = chart[i][j]
    # spin. sub2를 sub에 넣어준다.
    for i in range(length):
        for j in range(length):
            sub_chart[j][length-1-i]=sub2_chart[i][j]

    for i in range(start_row, start_row+length):
        for j in range(start_col, start_col+length):
            chart[i][j]=sub_chart[i-start_row][j-start_col]

def move(command):
    global n, chart
    if command == 0:
        return
    for row in range(0, n, 2**command):
        for col in range(0, n, 2**command):
            turn(row, col, 2**command)

def melt():
    global n, chart
    d_r=[1, -1, 0, 0]
    d_c=[0, 0, -1, 1]
    new_chart=deepcopy(chart)
    for row in range(n):
        for col in range(n):
            cnt=0
            for i in range(4):
                new_row=row+d_r[i]
                new_col=col+d_c[i]
                if 0<=new_row<n and 0<=new_col<n and chart[new_row][new_col]:
                    cnt+=1
            if cnt < 3:
                new_chart[row][col]=max(chart[row][col]-1, 0)
    chart=new_chart


for command in commands:
    move(command)
    #dump()
    melt()
    #dump()

summ=sum([k for c in chart for k in c])
print(summ)

ans=0

from collections import deque
def bfs(start_row, start_col):
    global n, visit

    que=deque()
    que.append((start_row, start_col))
    d_r=[-1, 1, 0, 0]
    d_c=[0, 0, -1, 1]
    cnt=1
    while que:
        now_row, now_col = que.popleft()
        for i in range(4):
            new_row=now_row+d_r[i]
            new_col=now_col+d_c[i]
            if 0<=new_row<n and 0<=new_col<n and not visit[new_row][new_col] and chart[new_row][new_col]:
                visit[new_row][new_col]=True
                que.append((new_row, new_col))
                cnt+=1
    return cnt


visit=[[False for i in range(n)] for j in range(n)]
for row in range(n):
    for col in range(n):
        if not visit[row][col] and chart[row][col] != 0:
            visit[row][col]=True
            ans=max(ans, bfs(row, col))
#dump()
print(ans)