from collections import deque
col_len, row_len = map(int, input().split())

chart=[]

for i in range(row_len):
    chart.append(list(input()))

visit=[[False for i in range(col_len)]for j in range(row_len)]

def counter(start_row, start_col):
    global row_len, col_len, chart, visit
    start_color=chart[start_row][start_col]
    que=deque()
    que.append((start_row, start_col))
    d_r=[1, -1, 0, 0]
    d_c=[0, 0 , -1, 1]
    counter=1
    while que:
        now_row, now_col = que.popleft()
        for i in range(4):
            new_row=now_row+d_r[i]
            new_col=now_col+d_c[i]
            if 0<=new_row<row_len and 0<=new_col<col_len and not visit[new_row][new_col] and chart[new_row][new_col] == start_color:
                visit[new_row][new_col]=True
                que.append((new_row, new_col))
                counter+=1
    
    return counter


b_count=0
w_count=0

for row in range(row_len):
    for col in range(col_len):
        if not visit[row][col]:
            visit[row][col]=True
            count=counter(row, col)
            #print(count)
            if chart[row][col] == 'B':
                b_count+=count**2
            else:
                w_count+=count**2

print(w_count, b_count)