from collections import deque

M, N = map(int, input().split())

visited = [[False for i in range(M)] for j in range(N)]
chart = []

ans = [0, 0]

def bfs(row, col, N, M, visited, chart):
    ret = 1
    que = deque()
    origin = chart[row][col]
    que.append((row, col))

    d_r = [0, 0, 1, -1]
    d_c = [1, -1, 0, 0]

    while que:
        r, c = que.popleft()

        for i in range(4):
            new_row = r + d_r[i]
            new_col = c + d_c[i]

            if 0<=new_row<N and 0<=new_col<M:
                if chart[new_row][new_col] == origin and not visited[new_row][new_col]:
                    visited[new_row][new_col] = True
                    que.append((new_row, new_col))
                    ret+=1

    return ret ** 2

for i in range(N):
    chart.append(list(input()))

for i in range(N):
    for j in range(M):
        if chart[i][j] == "W":
            chart[i][j] = 0
        else:
            chart[i][j] = 1

for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            visited[i][j] = True
            ans[chart[i][j]]+=bfs(i, j, N, M, visited, chart)

print(*ans)