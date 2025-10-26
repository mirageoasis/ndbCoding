import sys

n, m, k = map(int, input().split())
chart=[]

for i in range(n):
    chart.append(list(map(int, sys.stdin.readline().split())))

start=0
end=10**6+1
from collections import deque

while start < end:
    mid = (start+end)//2
    temp=0
    que=[]
    visit=[[False for i in range(m)]for j in range(n)]
    # 뚜껑
    for i in range(m):
        visit[0][i]=True
        if chart[0][i] <= mid: 
            que.append((0, i))
    # 옆기둥
    for i in range(n):
        visit[i][0]=True
        if chart[i][0] <= mid: 
            que.append((i, 0))
    for i in range(n):
        visit[i][m-1]=True
        if chart[i][m-1] <= mid: 
            que.append((i, m-1))
    que=deque(set(que))
    temp+=len(que)
    
    # mid 보다 크다면 que에 넣어주기
    d_r=[-1,1,0,0]
    d_c=[0,0,-1,1]
    while que:
        row, col = que.popleft()
        for i in range(4):
            new_row=row+d_r[i]
            new_col=col+d_c[i]
            if 0<=new_row<n and 0<=new_col<m and not visit[new_row][new_col]:
                visit[new_row][new_col]=True
                if chart[new_row][new_col] <= mid:
                    que.append((new_row, new_col))
                    temp+=1
    #print(temp, k, mid)
    if temp>=k:
        end=mid
    else:
        start=mid+1

print(start)
