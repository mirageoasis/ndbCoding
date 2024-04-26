import sys

N, M = map(int, input().split())

chart = []

for i in range(N):
    chart.append(list(map(int, sys.stdin.readline().split())))

visit = [[False for i in range(M)] for j in range(N)]

ans = -1

def dfs(N, M, depth, s, now_row, now_col, visit, chart):
    global ans
    dr = [0, 0, -1, 1]
    dc = [1, -1, 0, 0]
    if depth == 3:
        ans = max(ans, s)
        return
    if depth == 4:
        return

    for i in range(4):
        new_row = now_row + dr[i]
        new_col = now_col + dc[i]

        # 여러개를 선택하는 시나리오 ㄱ

        if  0 <= new_row < N and 0 <= new_col < M and not visit[new_row][new_col]:
            visit[new_row][new_col] = True
            dfs(N, M, depth+1, s+chart[new_row][new_col], new_row, new_col, visit, chart)
        
            for j in range(4):
                new_row_two = now_row + dr[j]
                new_col_two = now_col + dc[j]
                if  0 <= new_row_two < N and 0 <= new_col_two < M and not visit[new_row_two][new_col_two]:
                    visit[new_row_two][new_col_two] = True
                    dfs(N, M, depth+2, s+chart[new_row][new_col]+chart[new_row_two][new_col_two], new_row_two, new_col_two, visit, chart)
                    visit[new_row_two][new_col_two] = False
            
            visit[new_row][new_col] = False
        




# dfs를 하면서 depth가 4가 되면 값을 정산해서 최대값을 return
for i in range(N):
    for j in range(M):
        visit[i][j] = True
        dfs(N, M, 0, chart[i][j], i, j, visit, chart)
        visit[i][j] = False

print(ans)