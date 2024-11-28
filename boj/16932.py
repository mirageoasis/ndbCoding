import sys

n, m = map(int, input().split())
chart=[]
visit=[[False for i in range(m)] for j in range(n)]
for i in range(n):
    chart.append(list(map(int, sys.stdin.readline().split())))

ans=1
from collections import deque

def bfs(start_row, start_col, gp):
    global n, m
    que=deque()
    new_set=set()
    que.append((start_row, start_col))
    new_set.add((start_row, start_col))

    d_r=[1, -1, 0, 0]
    d_c=[0, 0, 1, -1]

    while que:
        now_row, now_col = que.popleft()
        for i in range(4):
            new_row=now_row+d_r[i]
            new_col=now_col+d_c[i]

            if 0<=new_row<n and 0<=new_col<m and not visit[new_row][new_col] and chart[new_row][new_col] == 1:
                visit[new_row][new_col]=True
                new_set.add((new_row, new_col))
                que.append((new_row, new_col))

    
    for r, c in new_set:
        #chart[r][c]=len(new_set)
        dot_gp[(r, c)]=gp
    gp_dict[gp]=len(new_set)

gp=1
gp_dict=dict()
dot_gp=dict()
for i in range(n):
    for j in range(m):
        if not visit[i][j] and chart[i][j] == 1:
            bfs(i, j, gp)
            gp+=1

for i in range(n):
    for j in range(m):
        if chart[i][j] == 0:
            temp=1
            d_r=[1, -1, 0, 0]
            d_c=[0, 0, 1, -1]
            to_add=set()
            for k in range(4):
                new_row=i+d_r[k]
                new_col=j+d_c[k]
                if 0<=new_row<n and 0<=new_col<m and chart[new_row][new_col] == 1:
                    to_add.add(dot_gp[(new_row, new_col)])
            
            for k in to_add:
                temp+=gp_dict[k]

            ans=max(temp, ans)


print(ans)