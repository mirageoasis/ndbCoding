#57
row_len, col_len = map(int, input().split())

chart=[]

for i in range(row_len):
    chart.append(list(input()))

visit=[[False for i in range(col_len)] for j in range(row_len)]

# * -> 물, X -> 돌, D-> 비버, S-> 두더지

#매 순간마다 물 먼저 계산
# 이후에 고슴도치 이동 계산

start_row, start_col = (0, 0)
end_row, end_col = (0, 0)

# start
for i in range(row_len):
    for j in range(col_len):
        if chart[i][j] == 'S':
            start_row=i
            start_col=j
            chart[i][j]='.'
            break
for i in range(row_len):
    for j in range(col_len):
        if chart[i][j] == 'D':
            end_row=i
            end_col=j
            chart[i][j]='.'
            break

from collections import deque
ans=-1
que=[]
que.append((start_row, start_col, 0))
visit[start_row][start_col]=True

while que:
    # 물 한번씩 퍼뜨리기
    
    li=[]
    dr=[1, -1, 0, 0]
    dc=[0, 0, 1, -1]
    for i in range(row_len):
        for j in range(col_len):
            if chart[i][j] == '*':
                li.append((i, j))
    # 물 설치 완료
    for r, c in li:
        for j in range(4):
            n_r=r+dr[j]
            n_c=c+dc[j]
            if 0<=n_r<row_len and 0<=n_c<col_len and chart[n_r][n_c]!='X' and not(n_r == end_row and n_c==end_col):
                chart[n_r][n_c]='*'
    
    move_list=[]

    for r, c, time in list(que):
        if r == end_row and c == end_col:
            ans=time
            break
        for i in range(4):
            n_r=r+dr[i]
            n_c=c+dc[i]
            if 0<=n_r<row_len and 0<=n_c<col_len and chart[n_r][n_c]!='X' and not visit[n_r][n_c] and chart[n_r][n_c] == '.':
                visit[n_r][n_c]=True
                move_list.append((n_r, n_c, time+1))
    
    que=move_list.copy()



if ans == -1:
    print("KAKTUS")
else:
    print(ans)