# 4시 11분
from sys import stdin
from collections import deque

# que에 벽 부순 횟수를 넣어준다.

row_len, col_len, lim = map(int, input().split())

chart=[]
visit=[[[False for i in range(col_len)] for j in range(row_len)] for k in range(lim+1)]

# for i in range(2):
#     print(visit[i])

for i in range(row_len):
    chart.append(list(map(int, list(stdin.readline().strip()))))

#print(visit[0][1])

#exit()

def bfs():
    global row_len, col_len, lim
    que=deque()
    # row, col, 벽 부순 횟수, 현재 횟수
    que.append((0, 0, 0, 1))
    visit[0][0][0]=True

    d_r=[1, -1, 0, 0]
    d_c=[0, 0, -1, 1]

    while que:
        now_row, now_col, now_crush, time=que.popleft()

        if now_row == row_len-1 and now_col == col_len-1:
            return(now_row, now_col, time)

        for i in range(4):
            new_row=now_row+d_r[i]
            new_col=now_col+d_c[i]

            if 0<=new_row<row_len and 0<=new_col<col_len and not visit[now_crush][new_row][new_col]:
                # 벽 부수기 가능
                # 벽 부수기 불가능
                if chart[new_row][new_col] == 0:
                    visit[now_crush][new_row][new_col]=True
                    que.append((new_row, new_col, now_crush, time+1))
                else:
                    if now_crush < lim:
                        visit[now_crush][new_row][new_col]=True
                        que.append((new_row, new_col, now_crush+1, time+1))
    
    return (-1, -1, -1)


a, b, ans = bfs()

print(ans)