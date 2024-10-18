from collections import deque

N=int(input())

chart=[]

for i in range(N):
    chart.append(list(input().strip()))

def dump_chart():
    for c in chart:
        print(c)

#dump_chart()

def bfs(start_row, start_col, visit):
    global N
    
    que=deque()
    que.append((start_row, start_col))
    alpha=chart[start_row][start_col]
    visit[start_row][start_col]=True

    d_r=[1, -1, 0, 0]
    d_c=[0, 0, -1, 1]

    while que:
        now_row, now_col= que.popleft()
        for i in range(4):
            new_row=now_row+d_r[i]
            new_col=now_col+d_c[i]

            if 0<=new_row<N and 0<=new_col<N and not visit[new_row][new_col] and chart[new_row][new_col] == alpha:
                visit[new_row][new_col]=True
                que.append((new_row, new_col))


# 처음 visit

f_visit=[[False for i in range(N)] for j in range(N)]

print()
# 나중 visit
# for 문 돌면서 R을 G로 바꾸기

f_cnt=1
for i in range(N):
    for j in range(N):
        if not f_visit[i][j]:
            bfs(i, j, f_visit)
            f_cnt+=1

#dump_chart()


for i in range(N):
    for j in range(N):
        if chart[i][j] == 'G':
            chart[i][j] = 'R'

s_visit=[[False for i in range(N)] for j in range(N)]

s_cnt=1
for i in range(N):
    for j in range(N):
        if not s_visit[i][j]:
            bfs(i, j, s_visit)
            s_cnt+=1
#print()
#dump_chart()

print(f_cnt-1, s_cnt-1)