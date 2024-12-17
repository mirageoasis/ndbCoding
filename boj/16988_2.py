from collections import deque
from itertools import combinations

row_len, col_len = map(int, input().split())

# 2가 어떻게 0을 만나는지 판단해야함

chart= []

for i in range(row_len):
    chart.append(list(map(int, input().split())))

def bfs(start_row, start_col):
    global row_len, col_len, chart, visit
    d_r=[1, -1, 0, 0]
    d_c=[0, 0, -1, 1]
    que=deque()
    que.append((start_row, start_col))
    visit[start_row][start_col]=True
    ret=1
    flag=True
    while que:
        now_row, now_col=que.popleft()
        for i in range(4):
            new_row=now_row+d_r[i]
            new_col=now_col+d_c[i]
            
            if 0<=new_row<row_len and 0<=new_col<col_len and not visit[new_row][new_col]:
                if chart[new_row][new_col]==0:
                    flag=False
                elif chart[new_row][new_col]==2:
                    visit[new_row][new_col]=True
                    que.append((new_row, new_col))
                    ret+=1

    return ret if flag else 0

candidate=[]
for i in range(row_len):
    for j in range(col_len):
        if chart[i][j] == 0:
            candidate.append((i, j))
ans=0
for first, second in combinations(candidate, r=2):
    
    chart[first[0]][first[1]]=1
    chart[second[0]][second[1]]=1
    
    temp=0
    visit=[[False for i in range(col_len)] for j in range(row_len)]
    for i in range(row_len):
        for j in range(col_len):
            if not visit[i][j] and chart[i][j] == 2:
                temp+=bfs(i, j)
    ans=max(ans, temp)
    chart[first[0]][first[1]]=0
    chart[second[0]][second[1]]=0

print(ans)