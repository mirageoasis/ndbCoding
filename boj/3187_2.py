from collections import deque

row_len, col_len = map(int, input().split())
chart=[]
visit=[[False for i in range(col_len)] for j in range(row_len)]

for i in range(row_len):
    chart.append(list(input()))

def bfs(start_row, start_col):
    global row_len, col_len, chart, visit
    que=deque()
    #print(chart[start_row][start_col])
    que.append((start_row, start_col))
    d_r=[1, -1, 0, 0]
    d_c=[0, 0, -1, 1]
    wolf_cnt=0
    sheep_cnt=0
    while que:
        now_row, now_col = que.popleft()
        if chart[now_row][now_col] == 'v':
            wolf_cnt+=1
        elif chart[now_row][now_col] == 'k':
            sheep_cnt+=1

        for i in range(4):
            new_row=now_row+d_r[i]
            new_col=now_col+d_c[i]

            if 0<=new_row<row_len and 0 <=new_col<col_len and not visit[new_row][new_col] and (chart[new_row][new_col] != '#'):
                visit[new_row][new_col]=True
                que.append((new_row, new_col))
    #print(sheep_cnt, wolf_cnt)
    if sheep_cnt > wolf_cnt:
        wolf_cnt=0
    else:
        sheep_cnt=0
    return (wolf_cnt, sheep_cnt)

wolf_total=0
sheep_total=0
for row in range(row_len):
    for col in range(col_len):
        if chart[row][col] != '#' and not visit[row][col]:
            visit[row][col]=True
            wf, sh = bfs(row, col)
            wolf_total+=wf
            sheep_total+=sh

print(sheep_total, wolf_total)