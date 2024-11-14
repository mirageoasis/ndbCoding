from collections import deque

# bfs 2번
# visit 처리

# visit 배열 숫자
N=int(input())
chart=[]


for i in  range(N):
    chart.append(list(map(int, input().strip().split())))


# for c in chart:
#     print(c)


def number_bfs(start_row, start_col, visit, height):
    global N
    que=deque()
    que.append((start_row, start_col))
    visit[start_row][start_col]=True

    d_r=[1, -1, 0, 0]
    d_c=[0, 0, -1, 1]
    #print(start_row, start_col)
    while que:
        now_row, now_col = que.popleft()

        for i in range(4):
            new_row=now_row+d_r[i]
            new_col=now_col+d_c[i]
            if 0<=new_row<N and 0<=new_col<N and not visit[new_row][new_col] and chart[new_row][new_col] <= height:
                que.append((new_row, new_col))
                visit[new_row][new_col]=True

def visit_bfs(start_row, start_col, visit):
    global N
    que=deque()
    que.append((start_row, start_col))
    visit[start_row][start_col]=True

    d_r=[1, -1, 0, 0]
    d_c=[0, 0, -1, 1]

    while que:
        now_row, now_col = que.popleft()

        for i in range(4):
            new_row=now_row+d_r[i]
            new_col=now_col+d_c[i]
            if 0<=new_row<N and 0<=new_col<N and not visit[new_row][new_col]:
                que.append((new_row, new_col))
                visit[new_row][new_col]=True

    
    pass
max_height=0
for i in range(N):
    for j in range(N):
        max_height=max(max_height, chart[i][j])

ans=0
for height in range(0, max_height+1):
    visit=[[False for i in range(N)] for j in  range(N)]

    # 방문 처리
    for i in range(N):
        for j in range(N):
            if chart[i][j] <=height and not visit[i][j]:
                number_bfs(i, j, visit, height)
    temp_ans=0
    # visit도 처리

    for i in range(N):
        for j in range(N):
            if not visit[i][j]:
                temp_ans+=1
                visit_bfs(i, j, visit)
    #print(height)
    ans=max(temp_ans, ans)

print(ans)