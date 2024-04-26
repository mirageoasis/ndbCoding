# bfs를 사용하는데 조건이 다음과 같다.

# 사방이 같은 번호면 취소

# 섬 번호 메기는 차트


import sys
from collections import deque

N = int(input())
# 판
chart = []
visited = [[False for i in range(N)] for j in range(N)]
now_number=1
for i in range(N):
    chart.append(list(map(int, sys.stdin.readline().split())))

def island_number(now_row, now_col, N, now_number, visited, chart):
    que = deque()

    visited[now_row][now_col] = True
    que.append((now_row, now_col))

    d_r = [-1, 1, 0, 0]
    d_c = [0, 0, -1, 1]

    while que:
        row, col = que.popleft()

        for i in range(4):
            new_row = row + d_r[i]
            new_col = col + d_c[i]
            if 0<=new_row<N and 0<=new_col<N and not visited[new_row][new_col] and chart[new_row][new_col]:
                visited[new_row][new_col] = True
                chart[new_row][new_col] = now_number
                que.append((new_row, new_col))


for i in range(N):
    for j in range(N):
        if chart[i][j] == 1 and not visited[i][j]:
            visited[i][j] = True
            chart[i][j] = now_number
            island_number(i, j, N, now_number, visited, chart)
            now_number+=1

# now_number 까지 살피면서 하기
            
# for c in chart:
#     print(*c)

# 0과 자신과 다른 숫자면 건넌다. 그리고 같은 숫자라면 stop한다.
INF=1000000
ans=INF

def bfs(island_number, N, chart, visited):
    INF=1000000
    que = deque()
    # row col dist

    for i in range(N):
        for j in range(N):
            if chart[i][j] == island_number:
                que.append((i, j, 0))
                visited[i][j] = True
    while que:
        row, col, dist = que.popleft()
        #print((row, col, dist))
        if chart[row][col] and chart[row][col] != island_number:
            return dist-1
        d_r = [-1, 1, 0, 0]
        d_c = [0, 0, -1, 1]

        for i in range(4):
            new_row = row + d_r[i]
            new_col = col + d_c[i]

            if 0<=new_row<N and 0<=new_col<N and chart[new_row][new_col] != island_number and not visited[new_row][new_col]:
                visited[new_row][new_col] = True
                que.append((new_row,new_col,dist+1))

for island_num in range(1, now_number):
    # 섬의 숫자
    for i in range(N):
        for j in range(N):
            visited[i][j] = False
    
    ret = bfs(island_num, N, chart, visited)
    #print(ret)
    ans = min(ans, ret)

print(ans)

