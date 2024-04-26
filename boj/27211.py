import sys
from collections import deque

N, M = map(int, input().split())

chart = []
visit = [[False for i in range(M)] for j in range(N)]
ans = 0

def converter(number, lim):
    if number == -1:
        return lim - 1
    if number == lim:
        return 0
    return number

def bfs(row_len, col_len, start_row, start_col, chart, visit):
    que = deque()
    que.append((start_row, start_col))
    d_r = [1, -1, 0, 0]
    d_c = [0, 0, -1, 1]

    while que:
        now_row, now_col = que.popleft()

        for i in range(4):
            new_row = converter(now_row+d_r[i], row_len)
            new_col = converter(now_col+d_c[i], col_len)

            if not visit[new_row][new_col] and chart[new_row][new_col] == 0:
                visit[new_row][new_col] = True
                que.append((new_row, new_col))


for i in range(N):
    chart.append(list(map(int, sys.stdin.readline().split())))

for i in range(N):
    for j in range(M):
        if chart[i][j] == 0 and not visit[i][j]:
            visit[i][j] = True
            bfs(len(chart), len(chart[0]), i, j, chart, visit)
            ans+=1

print(ans)