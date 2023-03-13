from collections import deque

chart = []
que = []
# k 이하의 자연수
N, K = map(int, input().split())

for _ in range(N):
    chart.append(list(map(int, input().split())))

S, X, Y = map(int, input().split())

for i in range(N):
    for j in range(N):
        if chart[i][j] != 0:
            que.append((chart[i][j], i, j, 0))

que.sort()
que = deque(que)

d_row = [1, -1, 0, 0]
d_col = [0, 0, -1, 1]

while que:
    virus_type, row, col, second = que.popleft()
    
    if(second == S):
        break
    for i in range(4):
        new_row = row + d_row[i]
        new_col = col + d_col[i]
        if -1 < new_col < N and -1 < new_row < N and chart[new_row][new_col] == 0:
            chart[new_row][new_col] = virus_type
            que.append((virus_type, new_row, new_col, second + 1))
    #print(que)

print(chart[X - 1][Y - 1])
