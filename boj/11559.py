from collections import deque

chart = []

COL_SIZE = 6
ROW_SIZE = 12
ans = 0

for i in range(12):
    chart.append(list(input().strip()))


def dfs(start_row, start_col, ROW_SIZE, COL_SIZE, now_count, chart, visited):
    que = deque()
    start_alpha = chart[start_row][start_col]
    que.append((start_row, start_col))

    dr = [1, -1, 0, 0]
    dc = [0, 0, -1, 1]

    while que:
        now_row, now_col = que.popleft()
        
        for i in range(4):
            new_row = now_row + dr[i]
            new_col = now_col + dc[i]

            if 0 <= new_row < ROW_SIZE and 0 <= new_col < COL_SIZE:
                if visited[new_row][new_col] == -1 and chart[new_row][new_col] == start_alpha:
                    visited[new_row][new_col] = now_count
                    que.append((new_row, new_col))



while True:
    # 없에기 -> 2 중 for문 돌리면서 dfs
    # column 마다 아래에서 count 해서 내려주기

    # 영역표시
    now_count = 0
    visited = [[-1 for i in range(COL_SIZE)] for j in range(ROW_SIZE)]
    for i in range(ROW_SIZE):
        for j in range(COL_SIZE):
            if visited[i][j] == -1 and chart[i][j] != '.':
                visited[i][j] = now_count
                dfs(i, j, ROW_SIZE, COL_SIZE, now_count, chart, visited)
                now_count+=1
    
    count_chart = [0 for i in range(now_count+1)]

    # 개수 세기
    for i in range(ROW_SIZE):
        for j in range(COL_SIZE):
            if visited[i][j] != -1:
                count_chart[visited[i][j]] +=1

    # 없에기
    for i in range(ROW_SIZE):
        for j in range(COL_SIZE):
            if visited[i][j] != -1 and count_chart[visited[i][j]] >= 4:
                chart[i][j] = '.'

    # 줄이기

    for i in range(COL_SIZE):
        starting = ROW_SIZE - 1
        for j in range(ROW_SIZE - 1, -1, -1):
            if chart[j][i] != '.':
                starting = j
                break

        for j in range(starting, -1, -1):
            if chart[j][i] != '.':
                alpha_max = j
                for k in range(ROW_SIZE - 1, j, -1):
                    if chart[k][i] == '.':
                        alpha_max = k
                        break
                tmp = chart[j][i]
                chart[j][i] = '.'
                chart[alpha_max][i] = tmp
    # print()
    # for c in chart:
    #     print(*c)
    # print()

    # for c in visited:
    #     print(*c)

            
    if max(count_chart) < 4:
        break
    ans+=1

print(ans)